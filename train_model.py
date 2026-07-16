import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
df = pd.read_csv(r"c:\Users\sanch\Downloads\student_data.csv")
print("\nDataset Loaded Successfully!\n")
print(df.head())
if "Student_Name" in df.columns:
    df = df.drop("Student_Name", axis=1)
required_columns = [
    "studytime",
    "absences",
    "G1",
    "G2",
    "G3"
]

for col in required_columns:
    if col not in df.columns:
        raise Exception(f"Column '{col}' not found in dataset.")

X = df[[
    "studytime",
    "absences",
    "G1",
    "G2"
]]

y = df["G3"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = RandomForestRegressor(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)
mse = mean_squared_error(y_test, predictions)
rmse = mse ** 0.5
r2 = r2_score(y_test, predictions)

print("\n========== MODEL PERFORMANCE ==========")
print(f"MAE  : {mae:.2f}")
print(f"MSE  : {mse:.2f}")
print(f"RMSE : {rmse:.2f}")
print(f"R²   : {r2:.2f}")

joblib.dump(model, "student_model.pkl")
joblib.dump(scaler, "scaler.pkl")

print("\nModel Saved Successfully!")
print("student_model.pkl")
print("scaler.pkl")

print("\nTraining Completed Successfully!")