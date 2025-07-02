# Breast Cancer Classifier

This project implements a very simple rule-based classifier to predict whether a tumor is malignant (`M`) or benign (`B`) based on various cell measurements. The classifier uses statistical thresholds derived from training data to make predictions on new cases.

## How It Works

- Reads and parses training and testing data files (`cancerTrainingData.txt`, `cancerTestingData.txt`).
- Trains a classifier using labeled training data.
- Predicts the class of each test record.
- Reports the accuracy of the classifier.

It is generally better to err on the side of caution in medical diagnostics. For example, adjusting the algorithm to predict "malignant" with a lower threshold may increase sensitivity, reducing the risk of missing true cases, even if it results in more false positives. Ultimately, tools like this should be used as part of a broader diagnostic process, not as the sole method for making critical decisions.

## Usage

1. Place the data files in the project directory.
2. Run:

   ```bash
   python cancer_classifier.py
   ```

3. The script will output the classification results and accuracy.

## Notes

- The classifier is intended as a demonstration and should not be used for real medical diagnosis.
- Data is based on the [UCI Machine Learning Repository Breast Cancer Wisconsin (Diagnostic) Data Set](https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+%28Diagnostic%29).

This code is provided for reference only. Please do not reuse or redistribute without permission.
