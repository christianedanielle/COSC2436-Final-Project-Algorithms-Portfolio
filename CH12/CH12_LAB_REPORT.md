# Chapter 12: Regression

## Student Information
- **Name:** Christiane Danielle  
- **Date:** May 7, 2026  
- **Course:** COSC 2436  

---

## Algorithm Summary
- **How it works:** K-Nearest Neighbors (KNN) regression predicts a numerical value by finding the k most similar data points to a new input and averaging their output values. In this lab, the model uses weather, weekend/holiday status, and game presence to estimate bakery loaf demand.
- **Time complexity:** Training is O(1) (lazy learning), while prediction is O(n × d), where n is the number of data points and d is the number of features.
- **When to use it:** KNN regression is used when predictions should be based on similarity to past examples, especially when relationships in data are non-linear and do not require a complex trained model.

---

## Test Results

| Input (Weather, Weekend/Holiday, Game) | Result | Notes |
|----------------------------------------|--------|-------|
| (4, 1, 0) | ~70.5 loaves | Prediction using k=4 |
| Dataset size | 20 rows | Training data size |


## Reflection Questions
1.What type of problem is this algorithm solving?
This is a supervised regression problem because the model is trained using labeled data to predict a continuous numerical output (loaves of bread).

2.Why is KNN considered a “lazy learning” algorithm?
KNN is called lazy learning because it does not build a model during training. Instead, it stores the dataset and performs computation only when making a prediction.

3.Why is feature scaling important in this dataset?
Feature scaling ensures that all variables contribute equally to distance calculations. Without scaling, one feature could dominate the result and reduce prediction accuracy.

##Challenges Encountered

One challenge was understanding how KNN calculates similarity using multiple features at once. It was also difficult to see how different values of k affect prediction stability. After testing, it became clear that smaller k values are more sensitive to noise, while larger k values produce smoother but less responsive predictions.
