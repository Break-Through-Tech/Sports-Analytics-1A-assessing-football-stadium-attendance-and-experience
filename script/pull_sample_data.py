"""
Pull one season of CFB game and venue data from the CFBD API, then get
weather for each game from Open-Meteo's free historical weather API
using each venue's lat/long and the game date. Saves each raw table
plus one merged CSV.

Usage:
    export CFBD_API_KEY="your_key_here"
    python pull_sample_data.py --year 2023
"""

import argparse
import os
import sys
import time

import pandas as pd
import requests

CFBD_URL = "https://api.collegefootballdata.com"
OPEN_METEO_URL = "https://archive-api.open-meteo.com/v1/archive"


def get_headers():
    api_key = os.environ.get("CFBD_API_KEY")
    if not api_key:
        sys.exit("Set the CFBD_API_KEY environment variable first.")
    return {"Authorization": f"Bearer {api_key}"}


def get_games(year, season_type="regular"):
    resp = requests.get(
        f"{CFBD_URL}/games",
        headers=get_headers(),
        params={"year": year, "seasonType": season_type, "classification": "fbs"},
    )
    resp.raise_for_status()
    return pd.DataFrame(resp.json())


def get_venues():
    resp = requests.get(f"{CFBD_URL}/venues", headers=get_headers())
    resp.raise_for_status()
    return pd.DataFrame(resp.json())


def get_weather_for_location(lat, lon, date_str, max_retries=3):
    """Return hourly temperature/precipitation/wind speed for one venue on one date."""
    params = {
        "latitude": lat,
        "longitude": lon,
        "start_date": date_str,
        "end_date": date_str,
        "hourly": "temperature_2m,precipitation,windspeed_10m",
        "timezone": "UTC",
    }
    for attempt in range(1, max_retries + 1):
        try:
            resp = requests.get(OPEN_METEO_URL, params=params, timeout=15)
            resp.raise_for_status()
            return resp.json().get("hourly", {})
        except requests.exceptions.RequestException as e:
            print(f"    attempt {attempt} failed for ({lat}, {lon}, {date_str}): {e}")
            time.sleep(2 * attempt)  # back off a bit longer each retry
    print(f"    giving up on ({lat}, {lon}, {date_str}), leaving it blank")
    return {}


def build_weather_table(games_with_coords):
    """One Open-Meteo call per unique (venue, date) pair, matched back to kickoff hour."""
    unique_locations = games_with_coords[
        ["venueId", "latitude", "longitude", "game_date"]
    ].drop_duplicates()

    total = len(unique_locations)
    rows = []
    for i, (_, loc) in enumerate(unique_locations.iterrows(), start=1):
        if i % 25 == 0 or i == total:
            print(f"    {i}/{total} venue/date combos done")
        hourly = get_weather_for_location(
            loc["latitude"], loc["longitude"], loc["game_date"]
        )
        rows.append(
            {
                "venueId": loc["venueId"],
                "game_date": loc["game_date"],
                "hourly_times": hourly.get("time", []),
                "hourly_temp": hourly.get("temperature_2m", []),
                "hourly_precip": hourly.get("precipitation", []),
                "hourly_wind": hourly.get("windspeed_10m", []),
            }
        )
        time.sleep(0.3)  # be polite to the free API

    return pd.DataFrame(rows)


def pick_kickoff_weather(row):
    """Use the kickoff hour (0-23, from startDate, UTC) to index into the hourly arrays."""
    if not isinstance(row["hourly_temp"], list) or len(row["hourly_temp"]) < 24:
        return pd.Series({"temperature_c": None, "precip_mm": None, "windspeed_kmh": None})

    kickoff_hour = int(row["startDate"][11:13])
    return pd.Series(
        {
            "temperature_c": row["hourly_temp"][kickoff_hour],
            "precip_mm": row["hourly_precip"][kickoff_hour],
            "windspeed_kmh": row["hourly_wind"][kickoff_hour],
        }
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--year", type=int, default=2023)
    parser.add_argument("--out", default="data")
    args = parser.parse_args()

    os.makedirs(args.out, exist_ok=True)

    print(f"Pulling {args.year} games...")
    games = get_games(args.year)
    games.to_csv(f"{args.out}/games_{args.year}.csv", index=False)
    print(f"  {len(games)} games saved")

    print("Pulling venues...")
    venues = get_venues()
    venues.to_csv(f"{args.out}/venues.csv", index=False)
    print(f"  {len(venues)} venues saved")

    merged = games.merge(
        venues, how="left", left_on="venueId", right_on="id", suffixes=("", "_venue")
    )
    merged["game_date"] = merged["startDate"].str[:10]

    has_coords = merged.dropna(subset=["latitude", "longitude", "startDate"])
    print(f"Pulling weather for {has_coords[['venueId', 'game_date']].drop_duplicates().shape[0]} unique venue/date combos...")
    weather_lookup = build_weather_table(has_coords)
    weather_lookup.to_csv(f"{args.out}/weather_{args.year}.csv", index=False)

    merged = merged.merge(weather_lookup, how="left", on=["venueId", "game_date"])
    merged[["temperature_c", "precip_mm", "windspeed_kmh"]] = merged.apply(
        pick_kickoff_weather, axis=1
    )

    merged.to_csv(f"{args.out}/merged_{args.year}.csv", index=False)
    print(f"  merged table saved: {len(merged)} rows, {len(merged.columns)} columns")


if __name__ == "__main__":
    main()