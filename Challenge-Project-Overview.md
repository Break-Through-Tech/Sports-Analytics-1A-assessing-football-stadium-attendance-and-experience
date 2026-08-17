---

> ## Challenge Advisor: Update & Finalize Your Project Overview
>
> > 💡 **These grey text instructions are just for you, the team's Challenge Advisor; please delete them once you have completed the steps below.**
>
> We've pre-populated this Challenge Project Overview page — which is what will be shared with your Break Through Tech student team in August — using the details from your submission form. You should have received an email inviting you to join this repo as a Collaborator, enabling you to add files and make edits.
> 
> In order for your project to be finalized and assigned to a team, please:
> 1. **Review all sections below** and update or expand any content as needed, making sure to address the SME Feedback in the section immediately below. Look for square brackets to find the places below that require additional inputs from you (e.g., "About [Company / Org Name]").
> 2. **Add your dataset** to the [data folder](data) in this repo.
> 3. **Close the Issue assigned to you in this repo** to let us know that you have made your edits and the overview page is ready for final review. You can do this by going to the _Issues_ tab in the top left section of the menu above, add a comment that says "CA review complete", and click the button to Close the Issue. 
>
> If you're unfamiliar with how to edit a page like this in GitHub, check out [this tutorial](https://ubc-lib-geo.github.io/gis-workshop-waml-template/content/handson/edit-readme.html) for a quick overview (start with step 2 and only edit this page), and [this guide](https://ubc-lib-geo.github.io/gis-workshop-waml-template/content/markdown.html) on how to use Markdown to compose text.
>
>
> ❌ Remember that this is a public repo. Do NOT include: Proprietary data, PII, API keys, credentials, or anything confidential.

---

### 🔍 SME Feedback from the Break Through Tech Evaluation Team

## 📋 BTT Internal Evaluation Notes
*(This section is for BTT staff and CAs only — remove before sharing with students)*

### Technical Vetting
| Check | Status | Notes |
| :--- | :--- | :--- |
| Python Compatibility | 🟢 | Project relies on standard libraries (pandas, scikit-learn, nltk/spacy) which are well-supported in Colab. |
| Data Readiness | 🟡 | Integrating multiple disparate APIs (Census, GTFS, Open-Meteo) significantly increases pre-processing burden for undergraduates. |
| Resource Check | 🟢 | Dataset size is small, and hardware requirements are compatible with Google Colab free tier. |

### Internal Scores
- **Student Fit Score:** 6/10
- **Technical Depth Score:** 7/10
- **Overall Recommendation:** REVISE

### Advisor Feedback Draft
This project offers a compelling use case for fan engagement, but the data acquisition strategy is overly complex for a 12-week sprint. I recommend focusing on one or two core data sources (e.g., nflverse reviews and pricing) to ensure depth over breadth. Please narrow the scope to a deterministic classification of 'high vs. low value' to allow students to prioritize model explainability and evaluation metrics over API integration maintenance.

---

# Assessing Football Stadium Attendance and Experience During the Regular Season

**Company / Org:** Other  
**Challenge Advisor:** Christina Coleman, coleman.chris.m@gmail.com  
**Program:** Break Through Tech AI Studio - Fall 2026  

---

## 🏢 About Other
Other is an independent initiative focused on enhancing sports fan engagement through data-driven insights. By analyzing the intersection of infrastructure, weather, and fan sentiment, the organization aims to optimize the gameday experience and improve overall stadium attendance.

---

## 🎯 The Challenge
### Project Summary
In this project, you will use stadium and venue review data (Kaggle-hosted datasets covering fan reviews, ratings, and gameday experience factors) and natural language processing and predictive modeling techniques (e.g., sentiment analysis, regression/classification) to build a model that scores whether a given game is 'worth attending' based on price, seat quality, and overall fan experience signals. This will help our company address the challenge of helping fans make informed decisions about ticket value, ultimately improving gameday attendance and satisfaction."

### Success Criteria

- Understanding of agile/scrum methodologies (understands basic terminologies and ceremonies applied throughout duration of the program)
- Team can confidently explain why they made decisions they did to get the model to its end state along the way
- Have a technical and non-technical understanding of the solution and use case (i.e. if communicating to non-technical audiences/final presentation prep)
- Model successfully produces outputs

### Project Milestones
Use these milestones to guide your work. Your team will create a GitHub Projects board to track tasks within each milestone.

| Month | Milestone | Key Activities |
|---|---|---|
| August | Challenge Setup & Team Onboarding | • Finalize challenge brief and dataset<br>• Draft rubric/success criteria for "worth attending" scoring model<br>• Onboard student teams; walk through problem statement and data |
| September | Exploratory Data Analysis & Feature Engineering | • Teams complete exploratory data analysis (EDA) on the review dataset<br>• Data cleaning and feature engineering (price, seat quality, sentiment signals)<br>• Checkpoint: teams present initial data insights |
| October | Baseline Modeling & Midpoint Review | • Baseline model development<br>• Midpoint check-in: model performance review, troubleshoot data gaps<br>• Begin iterating with sentiment components if using review text |
| November | Model Refinement & User-Facing Output | • Model refinement and validation<br>• Build out user-facing output (dashboard, score, or simple interface if necessary)<br>• Draft presentation/pitch narrative tying the model back to the business problem |
| December | Final Testing & Showcase | • Final testing<br>• Rehearse and deliver showcase presentation<br>• Submit final deliverable |

> **Note for the team:** Please create a GitHub Projects board in this repository to break these milestones into weekly tasks. Go to the **Projects** tab → **New project** → Choose **Board** → Add columns for each month.

---

## 📊 Dataset
**Name and Source:** 
- nflverse (2026 Games/Venue Schedule): https://github.com/nflverse/nfldata/commit/a0c82c889d4db5654dc72ed58acc2a73a6a2d3df
- nflreadpy: Python library 
- Open-Meteo: https://open-meteo.com/?utm_source=chatgpt.com
- Overpass API: https://overpass-api.de/?utm_source=chatgpt.com
- Ticketmaster API: https://developer.ticketmaster.com/products-and-docs/apis/discovery-api/v2/
- **Format:** CSV, JSON  
- **Size:** under 1gb  
- **Location:** see links above


### Key Details
- [Brief description of what's in the data]
- Data Limitations: Data is real but may potentially become outdated [Any known limitations or preprocessing needed]
- [Link to data dictionary or documentation, if available]

---

## 🛠️ Suggested Approach

**ML Problem Type:** Regression

**Recommended Libraries:**
- [e.g., pandas, scikit-learn, TensorFlow, Hugging Face]

**Evaluation Metrics:**
- Accuracy, Precision/Recall, RMSE, BLEU score
  
---

## 📚 Resources to Get Started

The following resources will help your team understand the problem space and potential technical approaches for this project:

**Background Reading:**
- [e.g., Link to an article or blog post about the problem domain]
- [e.g., Link to an industry report or case study]

**Technical Tutorials:**
- [e.g., Link to a free tutorial on the ML technique(s) involved]
- [e.g., Link to documentation for a key library or tool]

**Code Examples:**
- [e.g., Link to a relevant GitHub repo]
- [e.g., Link to a sample implementation or starter code]

**Other:**
- [Links to any additional resources — e.g., papers, videos, podcasts, etc.]

*Feel free to explore beyond these, and share anything interesting you find with me!*

---

## 🤝 How We'll Work Together

**Official check-ins:** During our biweekly 45-minute AI Studio Lab Section meeting block (2nd and 4th week of every month)

 **Other ways to reach out to me with questions:** 
* [e.g., Your team's channel within Break Through Tech’s Discord space]
* [e.g., Email; please copy your teammates and AI Studio Coach]
* [e.g., Request a team check-in on Zoom]
* [Note: I will aim to respond within 48 hours. Please reach out to your AI Studio Coach with urgent questions.]

> 💡 **Challenge Advisor: Please update the above based on your availability and preference. If you are not able to answer questions or meet with fellows outside of the biweekly Lab Section check-ins, simply write in "N/A (only available during the official check-in times)"**

**Recommended free coding / collaboration tools**
* […]
* […]

---

## 🚀 Getting Started

1. **Review this overview document** and note any questions for our first meeting
2. **Begin reviewing the dataset** using the link above
3. **Read the GitHub Projects documentation** [here](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects)

I’m excited to work with you!

---

## ❓ Questions?

Please bring any questions to our first meeting during the week of August 24th (Break Through Tech’s Bridge to Studio - Session C). 
