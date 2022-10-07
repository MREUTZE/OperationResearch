from gurobipy import *

# 创建名为BB的模型
BB = Model()
BB.setParam('LogToConsole',1)
# 定义b为约束右侧常数
b = [220, 280, 360, 140, 270]
# 定义变量x,y
V = [1, 2, 3, 4, 5]
A = [(i, j) for i in V for j in V if i <= j]
y = BB.addVars([1, 2, 3, 4, 5], vtype=GRB.BINARY, name='y')
x = BB.addVars(A, vtype=GRB.INTEGER, name='x')
# 定义目标函数
BB.setObjective(
    250 * quicksum(y[i] for i in range(1, 6)) + 2 * (quicksum(x[i, j] for i in range(1, 6) for j in range(i, 6)))
    + quicksum(x[i, i + 1] for i in range(1, 5)) + 2 * quicksum(x[i, i + 2] for i in range(1, 4)) + 3 * quicksum(
        x[i, i + 3] for i in range(1, 3)) + 4 * quicksum(x[i, i + 4] for i in range(1, 2)), sense=GRB.MINIMIZE)
# 定义约束条件
for j in range(1, 6):
    BB.addConstr(quicksum(x[i, j] for i in range(1, j + 1)) >= b[j - 1])
for i in range(1, 6):
    BB.addConstr(quicksum(x[i, j] for j in range(i, 6)) - 10000 * y[i] <= 0)
# 求最优解
BB.optimize()
BB.write('B&BE.lp')
# 输出结果
print('***************************')
print('最优解： ')
print('Z  = ', BB.ObjVal)  # 输出目标值
for v in BB.getVars():
    print(v.varName, ':', v.x)  # 输出变量值
print('***************************')
