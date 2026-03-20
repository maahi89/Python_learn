from sklearn.ensemble import RandomForestClassifier

# Input data
X = [[10], [15], [25], [30]]

# Output labels
y = ["Child", "Child", "Adult", "Adult"]

# Create model
model = RandomForestClassifier(n_estimators=10)

# Train model
model.fit(X, y)

# Predict
prediction = model.predict([[20]])

print(prediction)