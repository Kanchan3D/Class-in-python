class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myfunc(self):
        print("Hello my name is:"+self.name)
p1=person("John",36)
del p1.age
print(p1.name)
print(p1.age)
