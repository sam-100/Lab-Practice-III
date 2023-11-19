import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest, RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

# 1. Pre-process the dataset
df = pd.read_csv("your_dataset.csv")
df = df.drop(['irrelevant_column1', 'irrelevant_column2'], axis=1)
df = pd.get_dummies(df, columns=['categorical_column'])
df = df.dropna()

X = df.drop("fare_amount", axis=1)
y = df["fare_amount"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 2. Identify outliers
iso_forest = IsolationForest(contamination=0.05)
outliers = iso_forest.fit_predict(X_train_scaled)
X_train_cleaned = X_train_scaled[outliers != -1]
y_train_cleaned = y_train[outliers != -1]

# 3. Check the correlation
correlation_matrix = df.corr()
print(correlation_matrix)

# 4. Implement linear regression and random forest regression models
linear_model = LinearRegression()
linear_model.fit(X_train_cleaned, y_train_cleaned)

rf_model = RandomForestRegressor()
rf_model.fit(X_train_cleaned, y_train_cleaned)

# 5. Evaluate the models and compare their respective scores
def evaluate_model(model, X, y):
    y_pred = model.predict(X)
    r2 = r2_score(y, y_pred)
    rmse = mean_squared_error(y, y_pred, squared=False)
    return r2, rmse

linear_r2, linear_rmse = evaluate_model(linear_model, X_test_scaled, y_test)
rf_r2, rf_rmse = evaluate_model(rf_model, X_test_scaled, y_test)

print("Linear Regression - R2:", linear_r2, "RMSE:", linear_rmse)
print("Random Forest Regression - R2:", rf_r2, "RMSE:", rf_rmse)
