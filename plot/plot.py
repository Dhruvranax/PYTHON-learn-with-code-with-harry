#  this is not part of code with 100 days of code
# this part of oracle AI foundation course data visulization

import numpy as np 
import matplotlib.pyplot as plt  # ✅ correct import
from sklearn.datasets import make_circles

# Generate synthetic data
X, y = make_circles(n_samples=100, noise=0.1, factor=0.5, random_state=0)

# Plot
plt.figure(figsize=(8,6))
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='RdYlGn', edgecolors='k', marker='o', s=50)
plt.xlabel('Feature 1 (X[:, 0])')
plt.ylabel('Feature 2 (X[:, 1])')
plt.title('Plot of Points with Labels (make_circles Dataset)')
plt.colorbar(label='Class Label')
plt.show()
