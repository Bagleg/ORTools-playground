from ortools.sat.python import cp_model
# model.addWeightedSum()
model = cp_model.CpModel()

items = [(12, 4), (5, 3), (8, 5), (4, 2)]
weightLimit= 8
valueList = [item[0] for item in items]
weightList = [item[1] for item in items]
optimizedList = []
kept = [model.NewBoolVar("kept") for i in range(len(items))]
# maximizing the size of sum
goal = model.NewIntVar(0, sum(valueList), "goal")
model.Add(goal == sum(valueList[i] * kept[i] for i in range(len(items))))
model.Maximize(goal)
# ensuring weight is under limit
model.Add(sum(weightList[i] * kept[i] for i in range(len(items))) <= weightLimit)

solver = cp_model.CpSolver()
status = solver.Solve(model)

if status == cp_model.OPTIMAL:
    optimizedList = [items[i] for i in range(len(items)) if solver.Value(kept[i]) == 1]
    print(optimizedList)