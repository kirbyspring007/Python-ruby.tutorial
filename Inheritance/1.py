class class1(object):
    def method1(self):
        return 'm1'
c1 = class1()
print(c1, c1.method1())

class class3(class1):
    def method2(self):
        return 'm2'
c3 = class3()
print(c3, c3.method1())
print(c3, c3.method2())

class class2(object):
    def method1(self):
        return 'm1'
    def method2(self):
        return 'm2'
c2 = class2()
print(c2, c2.method1())
print(c2, c2.method2())
