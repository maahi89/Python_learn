from sklearn.linear_model import LogisticRegression

# Input data
X = [[1], [2], [3], [4]]

# Output labels (0 = Fail, 1 = Pass)
y = [0, 0, 1, 1]

# Create model
model = LogisticRegression()

# Train model
model.fit(X, y)

# Predict
prediction = model.predict([[2.5]])
print(prediction)