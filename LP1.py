from gurobipy import *

# 创建名为“model”的模型
model = Model()
# 定义参数
y1 = model.addVar(ub=GRB.INFINITY, lb=0, vtype=GRB.INTEGER, name="y1")
y2 = model.addVar(ub=GRB.INFINITY, lb=0, vtype=GRB.INTEGER, name="y2")
y3 = model.addVar(ub=GRB.INFINITY, lb=0, vtype=GRB.INTEGER, name="y3")
y4 = model.addVar(ub=GRB.INFINITY, lb=0, vtype=GRB.INTEGER, name="y4")
# 定义目标函数
model.setObjective(48*y1+20*y2+8*y3+5*y4, sense=GRB.MINIMIZE)
# 定义约束条件
model.addConstr(8*y1+4*y2+2*y3+0*y4 >= 60, name='CON1')
model.addConstr(6*y1+2*y2+1.5*y3+1*y4 >= 30, name='CON2')
model.addConstr(1*y1+1.5*y2+0.5*y3+0*y4 >= 20, name='CON3')
# 模型求解
model.optimize()
# 输出求解结果
print('***************************')
print('最优解： ')
print('Z  = ', model.ObjVal)  # 输出目标值
print('y1 =', y1.x)  # 输出 y1 的值
print('y2 =', y2.x)  # 输出 y2 的值
print('y3 =', y3.x)  # 输出 y3 的值
print('y4 =', y4.x)  # 输出 y4 的值
print('***************************')
