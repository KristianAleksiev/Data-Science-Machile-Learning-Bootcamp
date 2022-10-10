"""
# Make sample data

x_1 = np.array([[0.1, 1.2, 2.4, 3.2, 4.1, 5.7, 6.5]]).transpose() # 1d to 2d
y_1 = np.array([1.7, 2.4, 3.5, 3.0, 6.1, 9.4, 8.2]).reshape(7, 1) # 1d to 2d

regr = LinearRegression()
regr.fit(x_1, y_1)

print(f"MSE regression is: {mean_squared_error(y_1, regr.predict(x_1))}")

"""
