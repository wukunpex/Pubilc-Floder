class Teacher:
    school = 'old-boy'  # 也有相似的属性
    # 方便t1,t1,t3都能访问到次数，需要把这个属性变成类的数据属性
    count = 0  # 初始化count=0

    def __init__(self, name, sex, age, level, salary):  # 定义老师独有特征，年龄，性别
        # "__init__" 的意思是什么阶段就为对象添加自己独有的特征？
        # * 是在初始化阶段，是在第一次实例化的时候就为对象定义了自己独有的特征了，这是这个函数的意义所在 *

        self.name = name
        self.sex = sex
        self.age = age
        self.level = level
        self.salary = salary

        Teacher.count += 1  # 处理的时候用Teacher去处理，就能反应给所有的对象

    # 教学技能
    def teach(self):
        print('%s is teaching' % self.name)


# 每次实例化都能统计出来

t1 = Teacher('Shipping', 'male', 18, 10, 2000)
t2 = Teacher('xiaozhang', 'female', 18, 30, 12000)
t3 = Teacher('zhangming', 'male', 48, 3, 1000)

print(t1.count, t1.name, t1.salary, t1.age, t1.level, t1.sex)
print(t2.count, t2.name, t2.salary, t2.age, t2.level, t2.sex)
print(t3.count, t3.name, t3.salary, t3.age, t3.level, t3.sex)
