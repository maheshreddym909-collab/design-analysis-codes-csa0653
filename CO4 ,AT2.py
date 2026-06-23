NAME : S.VARUN RAM
  reg no : 192565023

                                                 1. WARE HOUSE ROUTE OPTIMIZATION :.


n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

edges = []

print("Enter u v weight:")
for i in range(e):
    u, v, w = map(int, input().split())
    edges.append([w, u, v])

edges.sort()

parent = []
for i in range(n):
    parent.append(i)

def find(x):
    while parent[x] != x:
        x = parent[x]
    return x

cost = 0

print("Edges in Minimum Spanning Tree:")

for w, u, v in edges:
    ru = find(u)
    rv = find(v)

    if ru != rv:
        parent[ru] = rv
        cost += w
        print(u, "-", v, "=", w)

print("Minimum Cost =", cost)

                                     2. MANUFACTURING RESOURCE ALLOCATION (DYNAMIC PROGRAMMING).

n = int(input())

inv = list(map(int, input().split()))
pro = list(map(int, input().split()))
name = input().split()
b = int(input())

inv = [i // 10000 for i in inv]
b = b // 10000

dp = [[0] * (b + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(b + 1):
        if inv[i - 1] <= j:
            dp[i][j] = max(dp[i - 1][j], pro[i - 1] + dp[i - 1][j - inv[i - 1]])
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[n][b])
