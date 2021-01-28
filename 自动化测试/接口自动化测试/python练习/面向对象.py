class MyClass:
    # 类简单示例
    i = 12345
    def f (self):
        return "hello word"

# 实例化类
x = MyClass()

# 访问类的属性与方法
print(x.i)

class people:
    #定义基本属性
    name = ''
    age = 0
    __weight = 0    
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self._weight = w
    def speak(self):
        print("%s说：我%d岁。"%(self.name,self.age))

class student(people):
    grade = ""
    def __init__(self,n,a,w,g):
        people.__init__(self,n,a,w)
        self.grade = g
    def speak(self):
        print("%s说，今年我%d岁了，我在读%s"%(self.name,self.age,self.grade))

class speaker():
    topic = ""
    name = ""
    def __init__(self,n,t):
        self.name = n
        self.topic = t 
    def speak(self):
        print("我是一个演说家，我的名字是%s,我今天演讲的主题是‘%s’"%(self.name,self.topic))


#多重继承
class sample(speaker,student):
    a = ""
    def __init__(self,n,a,w,g,t):
        speaker.__init__(self,n,t)
        student.__init__(self,n,a,w,g)
# p = people("tom",18,70)
# p.speak()

# s = student("tom",12,40,"三年级")
# s.speak()

# t = speaker("Aim","love")
# t.speak()
# 继承类

# s = sample("tom",15,50,"大三","love")
# s.speak()

class parent:
    def myMethod(self):
        print("调用父类方法")

class child(parent):
    def myMethod(self):
        print("调用子类方法")

c = child()
c.myMethod()
super(child,c).myMethod()