# TopBank Company - A Churn Prediction Project

   ![1_WqId29D5dN_8DhiYQcHa2w](https://user-images.githubusercontent.com/55566708/186330229-37e82b76-ffbe-48a3-8683-8b06ef2b3f44.png)


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

**TopBank** is a bank that operates in three European countries. Their main service is a bank account that works with other services as credit cards, payments and others. The contracts are valid for 12 moths, after one year the client could or not renovate it.


There's no charges for the bank services, the bank revenue come from operations with the client money deposited in the bank. Their analysts estimate that the bank profit is around 3% of gross annual salary for clients that earn below then the mean, and 5% for clients with annual salary above the mean.


In recent months TopBank noticed an accelerated growth in their churn's rate.


The challenge is understand the metrics that indicate a possible churn and help them to reduce the churn rate.


Marketing has a **$10,000** budget to work in an action trying retain the clients, we need to create a machine learning model the help the marketing team target the campaign as efficiently as possible.


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




**H2. Churn should occur for clients with high balance - TRUE**

- 39% of clients not in churn have balance equal to zero. 24% of clients in churn have balance equal to zero.
- The balance density distribution shows that as the balance value increases, the relative proportion of clients in churn is greater than the proportion of clients not in churn.
- The Balance group's relative percentage barplot shows that from balance 90,000 on, the relative percentage of clients in churn is greater than the relative percentage of clients not in churn.
- The correlation heatmap shows a correlation coefficient of 0.12 between balance and exited feature.
- Therefore, the hypothesis is true: churn occur for clients with high balance.
- 
![04_balance_density_distribution](https://user-images.githubusercontent.com/55566708/186326234-8fed4e80-b9eb-42aa-ba98-3d86a63267b7.png)
![04_balance_relative_percentage](https://user-images.githubusercontent.com/55566708/186326283-88644b9f-e9f7-457a-a098-dad5ddb7a92b.png)
![04_balance_heatmap](https://user-images.githubusercontent.com/55566708/186326308-79416374-9e96-411f-9b3a-67365157d387.png)

**Hypothesis 02:**



**H4. Churn should occur for clients with one product. - TRUE**

- Clients in churn: almost 70% have one product, 16.6% have two products, 10.4% have three products and 3% have four products.
- Clients not in churn: 53.4% have two products, 46% have one product, 0.6% have three products and none have four products.
- In absolute values, there are more clients in churn with three and four products than clients not in churn with three products. There are no clients not in churn with four products.
- Considering all clients with one product,  more than 70% are not in churn.
- Considering all clients with two products, more than 90% are not in churn.
- Considering all clients with three products, more than 80% are in churn.
- All clients that have four products are in churn.
- More than 50% of the clients have only one product.
- Therefore, the hypothesis is true: churn occur for clients with one product.

![04_num_products_percentage_product](https://user-images.githubusercontent.com/55566708/186326475-2ba0112d-0f72-4d2b-9136-7733ccc0b9cb.png)
![04_num_products_relative_percentage](https://user-images.githubusercontent.com/55566708/186326501-aeee11f6-72c4-4e55-a346-2a1796da3fed.png)


**Hypothesis 03:**




**H8. Churn rate should be higher for clients from Spain. - FALSE**

- 3993 clients (49.91%) are from France, 2005 clients (25.06%) are from Germany and 2002 clients (25.03%) are from Spain.
- Clients not in churn: 52.7% are from France, 26.2% are from Spain and 21.1% are from Germany. Compared to the whole dataset ratio, Germany decreased its proportion in aprox. 4%.
- Clients in churn: 40.7% are from Germany, 39% are from France and 20.3% are from Spain. Compared to the whole dataset ratio, - Germany increased its proportion in aprox. 15%. Conversely, Spain's ratio decreased in aprox. 5%.
- Therefore, the hypothesis is False: Churn rate is lower for clients from Spain.
- 
![04_geography_distribution_churn](https://user-images.githubusercontent.com/55566708/186327042-78154a3c-5bf9-46a7-aeeb-e4b8b8870309.png)
![04_geography_relative_percentage](https://user-images.githubusercontent.com/55566708/186327066-1276f6de-2d25-4c8b-b42c-cedc696c1cf5.png)


# 5. Machine Learning Model Applied
**Data Balance**
As the target variable (exited = 1) represents 20% of the total dataset, the SMOTETomek technique was applied in order to balance the train set. This technique is basically an oversampling with synthetic data generation (SMOTE (Synthetic Minority Oversmapling Technique)) + an undersampling (TOMEK Links).
After the resampling, the target variable ratio changed to 50 / 50:

![07_smotetomek](https://user-images.githubusercontent.com/55566708/186327290-035cbd21-3619-438b-8f5e-037162ac362b.png)

The following classifiers were trained in order to solve the churn prediction task.

Logistic Regression;
Random Forest;
XGBoost.

Two trains were performed: first with original imbalanced data, then with balanced data.
All the models were evaluated through 10-fold cross-validation on the train dataset.
The results are displayed below:

![07_models_balanced](https://user-images.githubusercontent.com/55566708/186327431-e880770a-ba0e-464b-9646-1ddb8e6f6174.png)

The models' overall performance improved significantly when trained with balanced data.
The Random Forest Classifier has the best recall (0.90) and F1-Score (0.89).
The XGBoost Classifier has the best precision (0.91), roc-auc-score (0.898) and MCC (0.80).
Based on the Business context and in order to better accomplish the project goals, deliverables and deployment, the chosen model to perform the fine tuning is Random Forest.



# 6. Machine Learning Modelo Performance

The Fine Tuning was performed using the Random Forest Classifier. Two fine-tuning were performed: the first with balanced data, and the second with imbalanced data.
A Randomized Search was executed through sklearn's RandomizedSearchCV function to perform the fine tuning.
The metrics were calculated using the test set, so that the models can be evaluated on unseen data, therefore a more realistic scenario.
The Random Forest with default hyperparameters, as well as the XGBoost, were also evaluated with their predictions on the test set for comparison purpose. The results are showed below:


![08_fine_tuning_summary](https://user-images.githubusercontent.com/55566708/186327549-00506c19-0723-4ef4-a57a-61cb5e86af6f.png)


The model with best performance, that is, with best F1-Score and best MCC is Random Forest tuned imb (Random Forest trained on original imbalanced data and fine-tuned).
What draws attention is the fact that the models trained with balanced data had a significant performance decrease on the test set compared to the metrics obtained with the train set, that is, the models overfitted the train data and could not generalize well on the test data, which means that it will have a poor performance on new data.


# 7. Business Results


All the business results were calculated on the test set.
As stated in the business challenge.
Bank account return per client:

- 15% for clients with estimated income lower than the average;
- 20% for clients with estimated income greater than the average.

**Revenue:**

- The total current return of all clients is 38,079,850.98.
- Total revenue loss if all 407 clients in churn leave the bank: 7,491,850.97.
- The total revenue loss represents 19.67% of total current return.

**Company's revenue , if the company avoids the customers to get into churn through the developed model:**

- Company's recovered revenue if 212 clients don't get into churn through the model: 4,064,569.35.
- That represents 52.09% of clients labeled as in churn and 54.25% of the total revenue loss.

This is an ideal scenario if the bank could give a gift or a financial incentive for all predicted clients in churn.
However, as stated in the business challenge, the amount available to give a financial incentive for the clients is constrained to 10,000, that is, is a limited resource that must be applied so that the return on investment (ROI) is maximized.
Furthermore, even if a client receives an incentive, it does not necessarily mean that this client will not leave the bank, hence a more realistic scenario must be built in order to deal with such situation.
The next step will show alternatives to deal with it.

### 7.1. Customer Incentive to Maximize ROI**

The Lift Curve and Cumulative Gains Curve showed that if the clients with the highest churn probability according the model's prediction are selected, then the gain over a random selection is maximized.
In this context, two scenarios were simulated: one with the top 100 clients with highest churn probability and the other with the top 200 clients.



The top 100 clients selection considered a financial incentive of $100 for each client, so that the available budget of $10,000 is not exceeded.
The revenue result was calculated as the following:

- Clients predicted as in churn and actually in churn (exited = 1): recovered revenue equal to the return that this clients gives to the bank.
- Clients predicted as in churn but actually not in churn (exited = 0): recovered revenue equal to zero, because the client would not leave the bank anyway (the incentive should be given to another client).
- The profit is the difference between recovered revenue and the incentive per client. Hence, clients with exited = 0 will generate a negative profit (investment loss).

**Top 100 Clients Results**

- Recovered Revenue: 1,672,172.96
- % Recovered from Total Revenue loss: 22.32%
- Investment: 10,000.00
- Profit: 1,662,172.96
- ROI: 16,621.73%
- Potential clients recovered acc. model: 93
- Potential churn reduction: 22.85%

Similarly, the top 200 clients selection considered a financial incentive of $50 per client, in order to not exceed the investment budget of $10,000.


**Top 200 Clients Results**

- Recovered Revenue: 3,089,126.96
- % Recovered from Total Revenue loss: 41.23%
- Investment: 10,000.00
- Profit: 3,079,126.96
- ROI: 30,791.27%
- Potential clients recovered acc. model: 159
- Potential churn reduction: 39.07%

The top 200 clients results are significantly better because it considers more clients than the previous scenario.


Nevertheless, the above-mentioned scenarios don't optimize the total revenue for the company. For example, if the top 100 clients are selected to receive a financial incentive, the return, say, of the 99th client can be much lower than the return of the 101th client that, in this case, would not be selected.


Considering the available budget of $10,000, and considering that to optimize the revenue it is necessary to select the clients with the highest return for the bank, and that these clients will receive an incentive to stay in the bank, what can be done to select such clients?
The approach to solve this problem is to use the "0-1 Knapsack Problem". Here's why:

- Goal: select the optimal combination of clients that maximize the total returned value , without exceeding the total weight constraint.
- In this case, each client has a "weight": the financial incentive that will be given in order to avoid the churn.
- The total weight constraint is the total amount available to give the incentives: $ 10,000.00.
- The incentive can either be offered or not: 0-1 (0-1 Knapsack).

A Knapsack function was created in the code to apply the 0-1 knapsack to the TopBank problem.
An incentive of $100 was considered in this first scenario.


**"0-1 Knapsack-Problem" approach Results**

- Recovered Revenue: 2,655,711.90
- % Recovered from Total Revenue loss: 35.45%
- Investment: 10,000.00
- Profit: 2,645,711.90
- ROI: 26,457.12%
- Potential clients recovered acc. model: 78
- Potential churn reduction: 19.16%

The result is much better compared to the top 100 clients scenario that gave also $100 incentive per client.


However, what if not all of these customers stay in the bank, even receiving an incentive? 

Also, could the incentive value be different, for example, for clients with a lower churn probability?


To answer this questions, a more realistic scenario was drawn considering these realistics aspects. The following premises were adopted:

- Some customers will leave no matter what: p(churn) > 0.99
- Some might stay but only with a $200 incentive: 0.95 < p(churn) < 0.99
- Some will stay with a $100 incentive: 0.90 < p(churn) < 0.95
- Others will stay with a $50 incentive: p(churn) < 0.90

Again, the knapsack approach was applied to select the clients that will provide the maximized revenue, considering the above-mentioned scenario.


**The Realistic Scenario with "0-1 Knapsack-Problem" approach Results**

- Recovered Revenue: 3,381,860.54
- % Recovered from Total Revenue loss: 45.14%
- Investment: 10,000.00
- Profit: 3,371,860.54
- ROI: 33,718.61%
- Potential clients recovered acc. model: 131
- Potential churn reduction: 32.19%

The realistic scenario obtained the best results compared to the previous scenarios.
It generates a profit of 3,371,860.54, 9.5% greater than the second best scenario profit of 3,079,126.96 (top 200 clients).
One interesting fact is that the potential clients recovered in the realistic scenario (131) is lower than the recovered clients of the top 200 scenario (159). Even so, the revenue of the realistic scenario is greater than the top 200. That shows that selecting the right clients brings the maximized revenue to the company instead of selecting the greatest number of clients.




That's beacuse the clients selection to deliver the maximized revenue is optimized.
Furthermore, three financial incentives were granted according to the churn probability. Specially the incentive of $50 for clients with churn probability lower than 0.90 probably considered a relevant number of clients. This is important because, for example, one client that receives a $100 incentive has the same investment of two clients that receive $50 each.

### 7.2. Business Performance Summary**


Business final results and answers to the business challenge questions.


**Business Questions**

- What's the company's current churn rate?
- How the churn rate varies per month?
- What's the model's performance to label the clients as churns?
- What's the company's revenue, if the company avoids the customers to get into churn through the developed model?
- Possible measure: discount coupon or other financial incentive. Which customers could receive an incentive and at what cost, in order to maximize the ROI (Return on investment)? (the sum of incentives shall not exceed $ 10,000.00).

**Business Results**

- The company's **current churn rate is 20%.**

- It is not possible to determine the churn variation per month, as the available data does not have information per month. What can be calculated is the churn variation per tenure (number of years that the customer was active). Note: this churn variation considers only the proportion of churn in the tenure itself.


![09_churn_tenure](https://user-images.githubusercontent.com/55566708/186328858-abd65bd6-350b-42b4-b4a1-03f4036af502.png)

- The model has a precision of 73.4% to label the clients as churns. The model can detect 52.1% of clients in churn.
- Total current revenue considering all clients: **38,079,850.98.**
- Total revenue loss if all 407 clients in churn leave the bank: **7,491,850.97 (19.67% of current total revenue).**


**Ideal Scenario according the model:**

- Company's revenue if 212 clients don't get into churn through the model: **4,064,569.35.**

- That represents **52.09% of clients** labeled as in churn and **54.25% of the total revenue loss.**


**Discount coupon or other financial incentive - Optimal Solution**

**Realistic Scenario (Alternative 4)**

Incentive value per client according model's predicted churn probability-range and maximum returned value with "0-1 Knapsack-Problem" approach.

- Recovered Revenue: 3,381,860.54
- **% Recovered from Total Revenue loss: 45.14%**
- Investment: 10,000.00
- **Profit: 3,371,860.54**
- ROI: 33,718.61%
- Potential clients recovered acc. model: 131
- **Potential churn reduction: 32.19%**


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
