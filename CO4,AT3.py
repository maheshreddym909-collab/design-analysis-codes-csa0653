NAME: S.VARUN RAM KUMAR
REG NO: 192565023
                 1.COMPARING GREEDY AND DYNAMIC PROGRAMMING FOR INVESTMENT PORTFOLIO OPTIMIZATION :

n = int(input())

name = []
capital = []
profit = []

for i in range(n):
    name.append(input())
    capital.append(int(input()))
    profit.append(int(input()))

budget = int(input())

# Greedy Method
ratio = []
for i in range(n):
    ratio.append((profit[i] / capital[i], capital[i], profit[i]))

ratio.sort(reverse=True)

g_profit = 0
g_budget = 0

for r, c, p in ratio:
    if g_budget + c <= budget:
        g_budget += c
        g_profit += p

print("Greedy Profit =", g_profit)

# Dynamic Programming
w = []
for i in range(n):
    w.append(capital[i] // 10000)

b = budget // 10000

dp = [0] * (b + 1)

for i in range(n):
    for j in range(b, w[i] - 1, -1):
        dp[j] = max(dp[j], dp[j - w[i]] + profit[i])

print("DP Profit =", dp[b])

                          2.COMPARING GREEDY AND DYNAMIC PROGRAMMING FOR DELIVERY VEHICLE LOADING

n = int(input())

w = []
p = []

for i in range(n):
    w.append(int(input()))
    p.append(int(input()))

c = int(input())

# Greedy
a = []
for i in range(n):
    a.append((p[i]/w[i], w[i], p[i]))

a.sort(reverse=True)

gw = gp = 0
for r, x, y in a:
    if gw + x <= c:
        gw += x
        gp += y

print("Greedy =", gp)

# Dynamic Programming
dp = [0] * (c + 1)

for i in range(n):
    for j in range(c, w[i]-1, -1):
        dp[j] = max(dp[j], dp[j-w[i]] + p[i])

print("DP =", dp[c])
