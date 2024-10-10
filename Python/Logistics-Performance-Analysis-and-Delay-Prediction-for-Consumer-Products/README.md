# Logistics Performance Analysis and Delay Prediction for Consumer Products

## Project Overview
In the competitive world of consumer products, efficient logistics are key to ensuring customer satisfaction and maintaining profitability. This project analyzes logistics performance and identifies factors contributing to delays, such as shipping modes, regions, and product categories. By building predictive models, we aim to classify orders into Delayed, On Time, or Early Arrival, helping businesses optimize their supply chain management. The insights gained will assist in minimizing disruptions and enhancing overall business performance.

## Objectives
- Gain insights into factors affecting delivery performance, such as regions, shipping modes, and product categories.
- Identify patterns in sales, profit, and customer behavior across different segments.
- Develop a predictive model to classify orders based on delivery status.
- Provide actionable recommendations to reduce delays and improve profitability.
- Create a Power BI dashboard for real-time visualization of logistics and performance metrics.

## Tools and Technologies
- **Python**: Data analysis, feature engineering, machine learning (using Pandas, NumPy, and Scikit-learn).
- **Data Visualization**: Seaborn, Matplotlib for trends and relationships visualization.
- **Machine Learning Models**: Decision Tree, Random Forest, AdaBoost, Gradient Boosting, and Stacking classifiers.
- **Jupyter Notebook**: For interactive analysis and reporting.
- **SSMS (SQL Server)**: Efficient data storage and retrieval.
- **Power BI**: For dynamic dashboard visualizing key metrics like order volume, sales, profitability, and delays.

## Data
The dataset used for this project comes from Kaggle, containing real-world logistics data with delivery labels indicating delay status. The data consists of various features, such as:
- Customer and order information
- Geographic and logistics data
- Product and category information
- Delivery labels (Delayed, On Time, Early Arrival)

## Key Analysis Insights
- **Order Volume**: Western Europe leads in order volume. The Consumer segment and Standard Class shipping mode dominate.
- **Sales Performance**: Categories like Fishing and Cleats contribute significantly to sales, with Europe and the Americas being top markets.
- **Profitability**: The highest profit margins are found in Europe and the U.S. Discount strategies need refinement as they lower profitability.
- **Order Delay**: Delays impact profits, particularly in Western Europe and Central USA. Standard Class shipping is profitable even with delays, but Same Day and First Class shipping lead to losses when delayed.

## Modeling
Several classification models were evaluated to predict delivery status, with Gradient Boosting and Stacking classifiers showing the best performance:
- **Gradient Boosting**: Train Accuracy: 70.04%, Test Accuracy: 69.67%
- **Stacking Classifier**: Train Accuracy: 70.23%, Test Accuracy: 69.82%
  
Both models performed well in predicting delayed orders, which are crucial for improving logistics performance.

## Conclusion
The project provides valuable insights into logistics optimization, with a focus on reducing delays and improving profitability. Shipping mode and regional factors play a significant role in delays, and predictive models offer moderate accuracy in classifying order delivery statuses.

## Power BI Dashboard
A Power BI dashboard is being developed to provide real-time insights and visualizations of key performance metrics.

## Dataset Link
[Kaggle Logistics Data](https://www.kaggle.com/datasets/pushpitkamboj/logistics-data-containing-real-world-data)
