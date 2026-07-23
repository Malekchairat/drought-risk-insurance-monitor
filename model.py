import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


def build_risk_model():
    # 1. Load the fetched data
    df = pd.read_csv("drought_data.csv")

    # 2. Feature Engineering: Actuarial Drought Index
    # High temp + Low precipitation = Higher Drought Risk
    # We create a synthetic target variable for risk classification:
    # 0 = Low Risk, 1 = Moderate Risk, 2 = High Risk (Drought / Claim potential)

    conditions = [
        (df["Max_Temp_C"] > 28) & (df["Precipitation_mm"] < 0.5),
        (df["Max_Temp_C"] > 22) & (df["Precipitation_mm"] < 2.0),
    ]
    choices = [2, 1]  # 2: High Risk, 1: Moderate Risk
    df["Risk_Level"] = np.select(conditions, choices, default=0)

    # Features and Target
    X = df[["Max_Temp_C", "Precipitation_mm"]]
    y = df["Risk_Level"]

    # 3. Train a Machine Learning Model (Random Forest Classifier)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    clf = RandomForestClassifier(n_estimators=50, random_state=42)
    clf.fit(X_train, y_train)

    # Predict risk for all records
    df["Predicted_Risk_Score"] = clf.predict_proba(X)[:, 2]  # Probability of High Risk

    print("✅ ML Model Trained Successfully!")
    print(df[["Region", "Date", "Max_Temp_C", "Precipitation_mm", "Risk_Level", "Predicted_Risk_Score"]].head())

    # Save enriched data for the dashboard
    df.to_csv("drought_processed.csv", index=False)


if __name__ == "__main__":
    build_risk_model()