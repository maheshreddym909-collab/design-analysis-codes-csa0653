NAME: S.VARUN RAM KUMAR
REG NO:192565023
                           1.Job Scheduling (Backtracking / NP-Hard Problem)
n = int(input())

jobs = []
emp = []

for i in range(n):
    jobs.append(input())

for i in range(n):
    emp.append(input())

used = [0] * n
ans = [""] * n

def solve(i):
    if i == n:
        return True

    for j in range(n):
        if used[j] == 0:
            used[j] = 1
            ans[i] = emp[j]

            if solve(i + 1):
                return True

            used[j] = 0

    return False

solve(0)

for i in range(n):
    print(jobs[i], "->", ans[i])


                             2.Exam Timetabling (Graph Coloring / NP-Complete Problem)

n = int(input())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

slot = [0] * n

def solve(v):
    if v == n:
        return True

    for c in range(1, n + 1):
        ok = True

        for i in range(n):
            if graph[v][i] == 1 and slot[i] == c:
                ok = False
                break

        if ok:
            slot[v] = c

            if solve(v + 1):
                return True

            slot[v] = 0

    return False

solve(0)

for i in range(n):
    print("Exam", i + 1, "-> Slot", slot[i])
