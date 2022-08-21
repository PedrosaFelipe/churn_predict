# TopBank Company - A Churn Prediction Project

**In this project, your mission will be to indicate to the company which customers will not renew their bank account in the next year, that is, which customers will enter a "churn" state. Its mission is to train an algorithm that identifies such customers and generates a score, indicating the probability of the customer not renewing the contract with the company. In addition, you need to think of an action plan to prevent these customers from not renewing.**

#### This project was made by Felipe Pedrosa.

## **Introduction**
- This repository contains the solution for this business problem (in portuguese): https://bit.ly/3ntCc6E
- This project is part of the "Data Science Community" (Comunidade DS), a study environment to promote, learn, discuss and execute Data Science projects. For more information, please visit (in portuguese): https://sejaumdatascientist.com/
- The goal of this Readme is to show the context of the problem, the steps taken to solve it, the main insights and the overall performance.


## **Project Development Method**
The project was developed based on the CRISP-DS (Cross-Industry Standard Process - Data Science, a.k.a. CRISP-DM) project management method, with the following steps:

- Business Understanding
- Data Collection
- Data Cleaning
- Exploratory Data Analysis (EDA)
- Data Preparation
- Machine Learning Modelling and fine-tuning
- Model and Business performance evaluation / Results

## **Table of Contents**

- [1. Business Problem](https://github.com/PedrosaFelipe/churn_predict/edit/main/README.md#1-business-problem)
- [2. Business Assumptions](https://github.com/PedrosaFelipe/churn_predict/edit/main/README.md#2-business-assumptions)
- [3. Solution Strategy](https://github.com/PedrosaFelipe/churn_predict/edit/main/README.md#3-solution-Strategy)
- [4. Top 3 Data Insights](https://github.com/PedrosaFelipe/churn_predict/edit/main/README.md#4-top-3-data-insights)
- [5. Machine Learning Model Applied](https://github.com/PedrosaFelipe/churn_predict/edit/main/README.md#5-machine-learning-model-applied)
- [6. Machine Learning Modelo Performance](https://github.com/PedrosaFelipe/churn_predict/edit/main/README.md#6-machine-learning-modelo-performance)
- [7. Business Results](https://github.com/PedrosaFelipe/churn_predict/edit/main/README.md#7-business-results)
- [8. Conclusions](https://github.com/PedrosaFelipe/churn_predict/edit/main/README.md#8-conclusions)
- [9. Lessons Learned](https://github.com/PedrosaFelipe/churn_predict/edit/main/README.md#9-lessons-learned)
- [10. Next Steps to Improve](https://github.com/PedrosaFelipe/churn_predict/edit/main/README.md#10-next-steps-to-improve)



# 1. Business Problem.

**The TopBank Company**

- A Bank Services Company, with main operations on Europe.
- Offers financial products such as bank account, investments and insurance.
- Business Model: banking services through physical agencies and online.
- Main Product: bank account without costs, valid for 12 months. After this period, the account must be renovated.
- Bank account revenue per client:

  - 15% of client's estimated salary, for clients with estimated income lower than the average;
  - 20% of client's estimated salary, for clients with estimated income greater than the average.



**Problem**

- Clients' cancellation rate increased significantly in the last few months.

**Goal**

- Reduce clients' churn rate, that is, to avoid that the client cancel the contract and don't renovate it for more 12 months.

**Deliverables**

- Model's performance and results report with the following topics:

  - What's the company's current churn rate?
  - How the churn rate varies per month?
  - What's the model's performance to label the clients as churns?
  - What's the company's revenue, if the company avoids the customers to get into churn through the developed model?


-Possible measure: discount coupon or other financial incentive.

  - Which customers could receive an incentive and at what cost, in order to maximize the ROI (Return on investment)? - The sum of incentives shall not exceed $ 10,000.00.

# 2. Business Assumptions.

# 3. Solution Strategy

My strategy to solve this challenge was:

**Step 01. Data Description:**

**Step 02. Feature Engineering:**

**Step 03. Data Filtering:**

**Step 04. Exploratory Data Analysis:**

**Step 05. Data Preparation:**

**Step 06. Feature Selection:**

**Step 07. Machine Learning Modelling:**

**Step 08. Hyperparameter Fine Tunning:**

**Step 09. Convert Model Performance to Business Values:**

**Step 10. Deploy Modelo to Production:**

# 4. Top 3 Data Insights

**Hypothesis 01:**

**True/False.**

**Hypothesis 02:**

**True/False.**

**Hypothesis 03:**

**True/False.**

# 5. Machine Learning Model Applied

# 6. Machine Learning Modelo Performance

# 7. Business Results

# 8. Conclusions

This project was developed in order to meet the TopBank's business challenge of churn prediction and to determine which clients should be contacted in order not to leave the bank and hence reduce the churn ratio.
The solution was built with a combination of machine learning algorithms that modelled the phenomenon and predicted the churn, as well as with an optimization algorithm based on the 0-1 Knapsack Problem to select the clients to receive a financial incentive not to leave the bank that maximizes the revenue for the bank.
The project delivers a model that has a precision of 73.4% and can detect 52.1% of clients in churn, recovers 45.14% of total revenue loss, enables a profit of $ 3,371,860.54 and gives a potential churn reduction of 32.19%.

The main challenges of the project were:

- The data with low variability with respect to positive and negative labels of the target variable: hard to find a pattern to distinguish them.
- The metrics used to evaluate the model can help calculating the business performance but cannot answer all the business questions, hence cannot meet all business results needs.
- Optimized solution to the business challenge outside the "Machine Learning Box".

Finally, the key point to improve the churn prediction and increase the revenue is in the model's performance: enhance the current model performance with new features / feature selection, experiment another models in order to achieve better performance, better evaluate the usage of balanced data to train the model. As the model improves its precision and recall, more clients can correctly be labeled as in churn and hence be contacted in order not to leave the bank, reduce the churn ratio and improve TopBank revenue.

# 9. Lessons Learned

 ## 9.1. What went wrong?

- Feature Engineering might be improved

The main goal of the feature engineering is to create features that better represent the phenomenon to be modelled, and therefore aid the model to learn and make improved predictions. In this project, as the original features were tightly mixed with respect to both labels of the target class, the feature engineering did not help to improve considerably the model performance, and/or did not find a pattern to distinguish positive and negative labels of the target variable.
Some features were created in order to find a pattern in the data to help the model to learn about the phenomenon, however the new features basically kept the same patterns from the original dataset features, which did not help the model to improve significantly its performance.
Actually, some of the new features created had more importance to the model than some original features, as checked in the feature selection step, therefore the new features helped somehow the model to have a better peformance that it would have only with the original features. The point here is that the feature engineering can be improved (in the next CRISP cycle for example) so that the model performance can also be improved significantly.

- Training on Balanced Data did not achieve the expected results

The model trained on balanced data did not achieve the expected results on the test set.
The dataset is imbalanced with respect to the target class: it has a ratio of 80/20. The dataset was balanced with the SMOTETomek technique in order to improve the model's performance. However, as the models trained on the balanced data improved significantly the metrics on the train set compared to the models trained on the original imbalanced data, they had poor performances when applied to the test set - it was expected a similar performance of the train set, which represents an overfitting. The reason for this behavour must be analysed in deeper detail, and is therefore one of the measures of the next steps.

- The "ordinary" model-assessment metrics did not help answering the business questions.

The model-assessment metrics such as F1-Score, Precision and ROC-AUC helped to compare the trained models and therefore to choose the better one to carry out the project predictions. Nevertheless, as the final Business Performance Step was achieved, it was realized that these model performance metrics could not answer the main business question of this project: "Which customers could receive an incentive and at what cost, in order to maximize the ROI (Return on investment)?". This is particularly specific of projects such churn prediction or marketing campaigns (that involves clients to be contacted), therefore additional metrics are needed to answer the business question.

 ## 9.2. What went right?

- Density plots showed that the features with high variability are the most relevants for the model.

The density plots were plotted with respect to the positive and negative labels of the target class. As they are normalized distributions, it is possible to check and compare the feature behavour for both labels. When both distributions are tightly overlapped, then it is harder for the model to distinguish the positive and negative labels with respect to that feature. However, when the distributions are detached, that is, when it is clear that the positive and negative labels distribution are not overlapped, then it is easier to distinguish both of them. What could be checked in this project is that even the slightest detachment of the target labels distribution of a feature determined it as an important feature for the model, as latter checked in the feature selection step (random forest's feature importance was used for that). Hence, the more variability of a feature with respect to the target class labels, the better for the model to model the phenomenon.

- Additional metrics to evaluate model performance according to the business challenge: lift curve and cumulative gains curve.

The metrics that helped to answer the main business question was the Lift curve and the cumulative gains curve, as they sort the predicted probability of each instance to belong to a label of the target class, and therefore can be used to prioritize the clients to be contacted. Also, they can be applied to compare the trained models, hence these are the specific metrics that can both compare models and answer the business question. The usage of such metrics depends on the business problem that the project is being designed for: for instance, if a project aims only to classify labels regardless of the prioritization, then these metrics are not mandatory to be used. However, if it involves prioritization such as clients to be contacted in a marketing campaign or to avoid churn, then these are the right metrics for both model performance evaluation and for answering the business question (which customers should be contacted?).

- Optimized solution to solve the business challenge: knapsack problem approach.

The knapsack problem approach was the perfect technique to optimize the results of the business challenge. That's because it has the following elements that fit in the business challenge proposal:
- Each element has a value. Business problem: each client provides a revenue for the bank;
- Each element has a weight. Business problem: each client will receive a financial incentive not to leave the bank;
- There is a constrained total weight. Business problem: the total amount for the financial incentive is $ 10,000.

With this reciprocal analysis it was possbile to apply the 0-1 knapsack problem approach to optimize the solution of the business problem. It is an exact optimal solution and an specific optimized algorithm. Hence, depending on the problem, the machine learning algorithms cannot provide the right answer for a specific business problem, and it is necessary to search outside the ML to find another technique to solve the problem.

9.3. What can be learned from this project?


- The new features created on the feature engineering might not help to characterize the phenomenon.


- The model trained on balanced data might fail on the test set.


- The "ordinary" model-assessment metrics might not answer the business questions.


- Density plots are a good way to check the target class variability and to evaluate the relevant features for the model.


- The Lift Curve and Cumulative Gains Curve are metrics to compare models' performance and can be used to prioritize clients to be contacted.


- The Knapsack-problem approach can be applied to solve and optimize a business problem.

# 10. Next Steps to Improve

The next steps of the project are listed below in priority order.
The goal of the next steps is to improve the model performance, hence to improve the business revenue / results.

- Better evaluate and experiment feature application in the current model in order to improve its results.
- Train another model in order to improve the overall performance: F1-Score, MCC, Precision and Recall.
- Data Balance experiment and evaluation.

# LICENSE

# All Rights Reserved - Comunidade DS 2022
