from gurobipy import *

# 创建名为BB的模型
BB = Model()
# 定义列表b为约束的常数项
b = [220, 500, 860, 1000, 1270]
# 定义变量x，y
y = BB.addVars([1, 2, 3, 4, 5], vtype=GRB.BINARY, name='y')
x = BB.addVars([1, 2, 3, 4, 5], vtype=GRB.INTEGER, name='x')
# 定义目标函数
BB.setObjective(250 * (quicksum(y[i] for i in range(1, 6))) + quicksum((8 - i) * x[i] for i in range(1, 6)) - 3850,
                sense=GRB.MINIMIZE)
# 定义约束条件
for j in range(1, 6):
    BB.addConstr(quicksum(x[i] for i in range(1, j + 1)) >= b[j - 1])
for i in range(1, 6):
    BB.addConstr(x[i] - 10000 * y[i] <= 0)
# 求最优解
BB.optimize()
# 输出结果
print('***************************')
print('最优解： ')
print('Z  = ', BB.ObjVal)  # 输出目标值
for v in BB.getVars():
    print(v.varName, ':', v.x)  # 输出变量值
print('***************************')
