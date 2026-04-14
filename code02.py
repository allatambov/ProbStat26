from scipy import stats
from matplotlib import pyplot as plt

### PART 01 ###

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

### PART 02 ###

X = stats.norm(loc = 100, scale = 20)
means9 = []

for i in range(1, 1001):
    sample = X.rvs(size = 9)
    mean = sample.mean()
    means9.append(mean)
print(len(means9))
print(means9)

plt.hist(means9, color = "cornflowerblue", edgecolor = "black");

means36 = []
for i in range(1, 1001):
    sample = X.rvs(size = 36)
    mean = sample.mean()
    means36.append(mean)
plt.hist(means36, color = "cornflowerblue", edgecolor = "black");

### PART 03 ###

Y = stats.uniform(20, 40)
print("Среднее генеральной совокупности:", Y.mean())
print("Стандартное отклонение генеральной совокупности:", Y.std())

r = Y.rvs(size = 10000)
plt.hist(r, color = "tomato", edgecolor = "black", density=True, bins = 4);
unif_means100 = []

for i in range(1, 1001):
    sample = Y.rvs(size = 100)
    mean = sample.mean()
    unif_means100.append(mean)
plt.hist(unif_means100, color = "tomato", edgecolor = "black");
