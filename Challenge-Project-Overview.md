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
This project leverages fan review datasets and multi-source API data—including weather, demographic, and transport metrics—to build a predictive model that identifies the value of attending specific NFL games. By applying natural language processing for sentiment analysis and classification/regression modeling, the team will develop a "worth attending" score to assist fans in making data-backed ticket purchasing decisions.

### Success Criteria
Model successfully produces outputs. Understanding of agile/scrum methodologies. Team can confidently explain why they made decisions they did to get the model to its end state. Have a technical and non-technical understanding of the solution and use case.

### Project Milestones
Use these milestones to guide your work. Your team will create a GitHub Projects board to track tasks within each milestone.
| Month | Milestone | Key Activities |
|-------|-----------|----------------|
| **September** | Data Exploration & Preprocessing | Import and normalize disparate datasets, conduct exploratory data analysis on fan reviews, and perform outlier detection on ticket pricing data. |
| **October** | Feature Engineering & Baseline Modeling | Engineer features from Open-Meteo and GTFS data; train baseline regression and classification models to identify primary value drivers. |
| **November** | Model Optimization & Evaluation | Execute hyperparameter tuning, conduct model validation against historical gameday data, and perform cross-validation to assess reliability. |
| **December** | Insights, Deliverables & Presentation | Finalize the predictive dashboard or interface, document business recommendations, and prepare the final presentation for stakeholders. |

> **Note for the team:** Please create a GitHub Projects board in this repository to break these milestones into weekly tasks. Go to the **Projects** tab → **New project** → Choose **Board** → Add columns for each month.

---

## 📊 Dataset
**Name and Source:** Stadium and Venue Review Datasets (nflverse, Open-Meteo, Census, GTFS)  
**Format:** CSV, JSON  
**Size:** under 1gb  
**Location:** Internal project folder/Kaggle Repository  

### Key Details
- Stadium and venue review data, including fan reviews, ratings, and gameday experience factors. Sources include nflverse, nflreadpy, Open-Meteo, OpenStreetMap Overpass API, Mobility Database GTFS.org, and U.S. Census Bureau API.
- Data requires normalization across disparate geographic and temporal scales; missing values in review text must be handled via NLP cleaning pipelines, while numeric API data requires interpolation for missing time-series points.

---

## 🛠️ Suggested Approach
**ML Problem Type:** Classification & Regression  
**Recommended Libraries:** Pandas, Scikit-learn, NLTK, Spacy, XGBoost  
**Evaluation Metrics:** Precision-Recall AUC for classification, Mean Absolute Error (MAE) for price/value regression, and F1-score for sentiment classification.

---

## 📚 Resources to Get Started
The following resources will help your team understand the problem space and potential technical approaches for this project:
**Background Reading:**
- NFL Analytics: Introduction to the `nflverse` ecosystem and its application in stadium data.
**Technical Tutorials:**
- Scikit-learn documentation on Classification and Regression pipelines for tabular datasets.
**Code Examples:**
- Sample GitHub repositories showcasing NLP sentiment analysis applied to review-based datasets.

---

## 🤝 How We'll Work Together
**Check-ins:** During our biweekly 60-min AI Studio Lab Section meeting block (2nd and 4th week of every month)  
**Communication:** Email and Slack workspace  
**Response time:** 48 hours  
**Recommended Tools:**
- **Coding:** Google Colab Free Tier  
- **Collaboration:** GitHub, Notion  
- **Virtual Meetings:** Zoom, Google Meet  

---

## 🚀 Getting Started
1. **Review this overview document** and note any questions for our first meeting.
2. **Begin reviewing the dataset** using the link provided in the Dataset section.
3. **Read the GitHub Projects documentation** [here](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/about-projects).

I'm excited to work with you!

---

## ❓ Questions?
Please bring any questions to our first meeting during the week of August 24th (Break Through Tech's Bridge to Studio - Session B).
