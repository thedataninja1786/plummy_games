import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

data = {
    "Report Month": ["2024-12", "2024-11", "2024-10", "2024-09", "2024-08", "2024-07", "2024-06", 
                     "2024-05", "2024-04", "2024-03", "2024-02", "2024-01"],
    "Total Cost": [9108.96, 10011.59, 18336.47, 21402.19, 26576.44, 14858.04, 19050.05, 
                   22658.09, 24920.71, 31358.28, 31789.54, 26127.75],
    "Total Installs": [2350, 1310, 2809, 3288, 4595, 3849, 3864, 3801, 3074, 6013, 13016, 11468],
    "ARPU D30": [1.31, 2.39, 1.74, 1.80, 1.67, 1.44, 1.78, 1.44, 1.36, 1.49, 0.75, 0.76],
    "ARPU D60": [1.47, 4.15, 2.81, 2.94, 2.22, 2.49, 2.84, 2.78, 2.07, 2.22, 1.03, 1.29],
    "ARPU D90": [1.47, 4.97, 3.78, 3.56, 2.93, 3.19, 3.67, 3.56, 2.57, 2.86, 1.23, 1.65],
    "ARPU D180": [1.47, 4.97, 4.16, 4.17, 4.09, 4.11, 5.11, 4.30, 3.46, 3.89, 1.63, 2.13]
}

# TASK
# Using the available data, forecast ROAS D180 for each month

df = pd.DataFrame(data)
df["Report Month"] = pd.to_datetime(df["Report Month"], format="%Y-%m")
df = df.sort_values(by=["Report Month"])

df["Revenue D180"] = df["Total Installs"] * df["ARPU D180"]

# use the first 6 months which are complete
X = df[["Total Cost"]].to_numpy()
Y = df.loc[:6, "Revenue D180"].to_numpy()

X = X.reshape(-1,1)
Y = Y.reshape(-1,1)

model = LinearRegression()

for i in range(len(Y), len(X)):
    X_subset = X[:i]
    model.fit(X_subset, Y)
    y_pred = model.predict(X[i].reshape(1, -1))
    Y = np.append(Y, y_pred).reshape(-1, 1)

df["Predicted Revenue D180"] = Y
df["Predicted Revenue D180"] = df["Predicted Revenue D180"].apply(lambda x: round(x,2))
df["ROAS D180"] = (df["Predicted Revenue D180"] / df["Total Cost"])*100
df["ROAS D180"] = df["ROAS D180"].apply(lambda x:round(x,2))

# Plot 
plt.figure(figsize=(10, 5))
plt.plot(df["Report Month"], df["Total Cost"], marker="o", label="Total Cost", color="red")
plt.plot(df["Report Month"], Y, marker="o", label="Revenue D180")

plt.plot(df["Report Month"].iloc[6:], Y[6:], marker="o", label="Predicted Revenue D180", color="green")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout(pad=1.5)
plt.savefig("forecasted_roas_d180.png")
plt.show()
