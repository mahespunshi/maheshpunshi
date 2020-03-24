#implicit inheritance

class Parent(object):
    def implicit(selfs):
        print("Parent implicit()")

class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

# override explicitly

class Parent(object):
    def override(self):
        print("Parent override()")
class Child(Parent):
    def override(self):
        print("Child override()")
dad = Parent()
son = Child()

dad.override()
son.override()

# Alter before or After
class Parent(object):
    def altered(self):
        print("Print altered()")

class Child(Parent):
    def altered(self):
        print("Child, Before Parent altered()")
        super(Child,self).altered()
        print("Child, After parent altered()")

dad = Parent()
son = Child()

dad.altered()
son.altered()
