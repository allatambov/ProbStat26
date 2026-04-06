from scipy import stats
from matplotlib import pyplot as plt

S = stats.binom(n = 10, p = 0.7)
print(S)
print("Математическое ожидание:", S.expect())
print("Дисперсия:", S.var())

print(S.pmf(0))
print(S.pmf(7))

values = range(0, 11)
print(*values)

probs = S.pmf(values).round(4)
print(*probs)

plt.vlines(values, ymin = 0, ymax = probs, 
           colors = "firebrick", linewidths = 2);
plt.grid();

N = 50
P = 0.7

x = stats.binom(n = N, p = P)
x_values = range(0, N + 1)
x_probs = x.pmf(x_values).round(4)

plt.vlines(x_values, ymin = 0, ymax = x_probs, 
           colors = "firebrick", linewidths = 2);
plt.grid();
