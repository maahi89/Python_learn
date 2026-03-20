from sklearn.tree import DecisionTreeClassifier

# Input data (age)
X = [[10], [15], [25], [30]]

# Output labels
y = ["Child", "Child", "Adult", "Adult"]

# Create model
model = DecisionTreeClassifier()

# Train model
model.fit(X, y)

# Predict
prediction = model.predict([[20]])
print(prediction)