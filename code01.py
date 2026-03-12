import numpy as np
from scipy import stats
from matplotlib import pyplot as plt

X = stats.norm(loc = 120, scale = 15)
print(X.pdf(120))
print(X.pdf(190))

x_vals = np.linspace(120 - 3 * 15, 120 + 3 * 15, num = 100)
print(x_vals[0:4])

density = X.pdf(x_vals)
print(density[0:4])

plt.plot(x_vals, density, color = "black");
plt.grid();
plt.ylabel("Плотность распределения");

interval01 = np.linspace(130, 120 + 3 * 15, num = 100)
density01 = X.pdf(interval01)

plt.plot(x_vals, density, color = "black");
plt.fill_between(interval01, density01, color = "red", alpha = 0.5);
plt.grid();
plt.ylabel("Плотность распределения");

print(1 - X.cdf(130))










