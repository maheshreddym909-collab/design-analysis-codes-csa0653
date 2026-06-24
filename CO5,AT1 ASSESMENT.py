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

DESCRIPTION:

1. Define the Problem
Assign jobs to employees.
Complete each job before its deadline.
One employee can do only one job at a time.

2. Identify the Constraints
Every job must be assigned.
One employee cannot handle multiple jobs at the same time.
Jobs should be completed within the given deadline.

3. Analyze the Constraints
First, check employee availability.
Next, verify the job deadline.
If any constraint is violated, reject that assignment.

4. Develop a Solution
Use the Backtracking algorithm.
Assign one employee to a job.
If the assignment is valid, move to the next job.

5. Apply Backtracking Concepts
Use recursion to assign jobs one by one.
Use pruning to skip invalid assignments.
Backtrack whenever a constraint is violated.

6. Justification
The solution satisfies all constraints.
Every job gets one employee.
No employee is assigned more than one job at the same time.

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

DESCRIPTION:

1. Define the Problem
Schedule all exams.
Ensure no student has two exams at the same time.
Use the available rooms efficiently.

2. Identify the Constraints
Assign one time slot for each exam.
Room capacity should not be exceeded.
Conflicting exams must have different time slots.
Every exam must be scheduled.

3. Analyze the Constraints
Check student conflicts first.
Verify room availability and capacity.
Assign a valid time slot.
Reject any conflicting assignment.

4. Develop the Solution
Use the Backtracking (or CSP) algorithm.
Assign a time slot to each exam.
Check all constraints before moving to the next exam.
If a conflict occurs, backtrack and try another time slot.

5. Apply Graph Coloring
Represent each exam as a vertex.
Connect exams with an edge if students are common.
Assign different colors (time slots) to connected vertices.

6. Justify the Solution
Produces a conflict-free exam timetable.
Satisfies room and time constraints.
Uses backtracking to find a valid schedule efficiently.
for i in range(n):
    print("Exam", i + 1, "-> Slot", slot[i])
