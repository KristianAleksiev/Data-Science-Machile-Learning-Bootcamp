"""
1. Importing pandas, matplotlib and scikit-learn

import pandas
from pandas import DataFrame
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

2. Reading the data:

data = pandas.read_csv("")
data.describe()
X = DataFrame(data, columns=[""])
y = DataFrame(data, columns=[""])

3. Plotting the data:

plt.figure(figsize=(10, 6)) - Setting up the show window
plt.scatter(X, y, alpha=0.3) - Transparency of the data points
plt.title("") - Title of chart
plt.xlabel("") - Label of x coordinates
plt.ylabel("") - Label of y coordinates
plt.ylim(0, 5) - Limiter min/max y axis
plt.xlim(0, 5) - Limiter mix/max x axis
plt.show() - Show the plotted table

4. Plotting the Regression Model:

regression = LinearRegression()
regression.fit(X, y)

5. Calculating the slope coefficient (Theta one):

regression.coef_

6. Calculating the Interception:
regression.intercept_

7. Plotting the data with the line of regression:

plt.figure(figsize=(10, 6))
plt.scatter(X, y, alpha=0.3)
plt.plot(X, regression.predict(X), color="red", linewidth=4) <======
plt.title("Movie Cost vs Global Revenue")
plt.xlabel("Budget ($)")
plt.ylabel("Global Revenue")
plt.ylim(0, 3000000000)
plt.xlim(0, 450000000)
plt.show()

8. Exporting the chars:
%matplotlib inline
"""
