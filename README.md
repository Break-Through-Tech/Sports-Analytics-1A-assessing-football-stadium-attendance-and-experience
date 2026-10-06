# Sport Analytics: Assessing Football Stadium Attendance and Experience

> 💡 **Note for the team:** This is just a template. Update the above title with your AI Studio Challenge Project name. Remove all guidance notes and example text in this template and populate this README with your own content. You can work on this README throughout AI Studio, and get feedback from your AI Studio Coach and Challenge Advisor before finalizing it.  

---

### 👥 **Team Members**

**Example:**

| Name             | GitHub Handle | Contribution                                                             |
|------------------|---------------|--------------------------------------------------------------------------|
| Hung Le    | @Hungoliann | Data exploration, visualization, overall project coordination            |
| Angel Chen   | @AngelChen914     | Data collection, exploratory data analysis (EDA), dataset documentation  |
| Bhaumi Nadella     | @Bhaumii  | Data preprocessing, feature engineering, data validation                 |
| Jameilynn Sibri     | @jamei-iiii    | Model selection, hyperparameter tuning, model training and optimization  |
| Samil Rodriguez       | @SalmonSalado    | Model evaluation, performance analysis, results interpretation           |

---

## 🎯 **Project Highlights**

**Example:**

- Developed a machine learning model using `[model type/technique]` to address `[challenge project task]`.
- Achieved `[key metric or result]`, demonstrating `[value or impact]` for `[host company]`.
- Generated actionable insights to inform business decisions at `[host company or stakeholders]`.
- Implemented `[specific methodology]` to address industry constraints or expectations.

---

## 👩🏽‍💻 **Setup and Installation**

**Provide step-by-step instructions so someone else can run your code and reproduce your results. Depending on your setup, include:**

* How to clone the repository
* How to install dependencies
* How to set up the environment
* How to access the dataset(s)
* How to run the notebook or scripts

---

## 🏗️ **Project Overview**

**Describe:**

- How this project is connected to the Break Through Tech AI Program
- This project connects to the Break Through Tech AI program because it provides an opportunity to showcase the knowledge and skills that were developed during the Summer Machine Learning Foundations course. 
- Your AI Studio host company and the project objective and scope
- The real-world significance of the problem and the potential impact of your work

---

## 📊 **Key Findings From EDA**

Data: 2,021 FBS home games (2024–2026 seasons). 1,673 have a usable high_attendance label (≥90% of capacity), and 44% of those are high-attendance.

Stadium capacity is the strongest predictor of attendance (correlation 0.92), but some large stadiums still draw well below their size.
Team strength matters. Home pregame Elo correlates at 0.72 and away pregame Elo at 0.37.
Conference splits attendance sharply. The SEC (~79k) and Big Ten (~65k) lead; the MAC and C-USA trail at ~14k.
Weather has almost no effect. Temperature, precipitation and wind all correlate near zero.
Attendance is right-skewed. The median is ~36k, while a few games top 100k.

Data quality: 14% of games are missing attendance. 308 games exceed listed capacity, likely due to outdated capacity figures; this doesn't affect the label.

Takeaway: Venue, conference and team strength should be the core features; weather adds little.

---

## 🧠 **Model Development**

**You might consider describing the following (as applicable):**

* Model(s) used (e.g., CNN with transfer learning, regression models)
* Feature selection and Hyperparameter tuning strategies
* Training setup (e.g., % of data for training/validation, evaluation metric, baseline performance)


---

## 📈 **Results & Key Findings**

**You might consider describing the following (as applicable):**

* Performance metrics (e.g., Accuracy, F1 score, RMSE)
* How your model performed
* Insights from evaluating model fairness

**Potential visualizations to include:**

* Confusion matrix, precision-recall curve, feature importance plot, prediction distribution, outputs from fairness or explainability tools

---

## 🚀 **Next Steps**

**You might consider addressing the following (as applicable):**

* What are some of the limitations of your model?
* What would you do differently with more time/resources?
* What additional datasets or techniques would you explore?

---

## 📝 **License**

Specify how your project can be used by others. Choose an appropriate license and link it here (e.g., MIT, Apache 2.0). Make sure your Challenge Advisor approves of the selected license type. 

**Example:**
This project is licensed under the MIT License.

---

## 📄 **References** (Optional but encouraged)

Cite relevant papers, articles, or resources that supported your project.

---

## 🙏 **Acknowledgements** (Optional but encouraged)

Thank your Challenge Advisor, host company representatives, TA, and others who supported your project.
