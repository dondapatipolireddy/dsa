INHERITANCE:

n Python, you can access parent class attributes (variables/methods) in several simple ways.

🟦 1. Direct access (inheritance)

If a child inherits a parent, it can directly use parent attributes:

class Parent:
    def __init__(self):
        self.name = "Parent Name"

class Child(Parent):
    pass

c = Child()
print(c.name)

👉 Output:

Parent Name
🟩 2. Using super() (BEST PRACTICE)

Used when child has its own constructor but still wants parent attributes.

class Parent:
    def __init__(self):
        self.name = "Parent Name"

class Child(Parent):
    def __init__(self):
        super().__init__()   # call parent constructor
        self.age = 20

c = Child()
print(c.name)
print(c.age)
🧠 Why super()?

✔ Ensures parent initialization runs
✔ Avoids duplicate code
✔ Important in multiple inheritance

🟨 3. Accessing parent class variable directly

If attribute is class-level:

class Parent:
    city = "Chennai"

class Child(Parent):
    pass

print(Child.city)
🟧 4. Using ParentClass name directly

You can explicitly call parent attributes/methods:

class Parent:
    def show(self):
        print("Parent method")

class Child(Parent):
    def show(self):
        Parent.show(self)   # direct parent call
        print("Child method")

c = Child()
c.show()
⚡ Output:
Parent method
Child method
🧠 Summary (VERY IMPORTANT)

You can get parent attributes using:

✔ Direct inheritance → child.attribute
✔ super().__init__() → initialize parent attributes
✔ ParentClass.attribute → direct access
✔ super().method() → preferred method call

🧠 Interview Answer:

In Python, parent class attributes can be accessed directly through inheritance, or by using super() to call the parent constructor. We can also access them using the parent class name explicitly, depending on the design.

If you want next, I can explain:
✔ super() vs ParentClass.name (very important confusion)
✔ multiple inheritance attribute resolution (MRO)
✔ tricky interview questions on inheritance + attributes

MEHTOD HOWS GET

You are asking: “How are methods of parent class accessed (got) in Python?”

Here is the clear explanation 👇

🟦 1. Direct access through inheritance

If a child class inherits a parent class, it can directly use parent methods.

class Parent:
    def show(self):
        print("Parent method")

class Child(Parent):
    pass

c = Child()
c.show()

👉 Output:

Parent method

✔ No need to define again in child class

🟩 2. Overriding + using parent method

If child has same method name, it overrides parent method.

class Parent:
    def show(self):
        print("Parent method")

class Child(Parent):
    def show(self):
        print("Child method")

c = Child()
c.show()

👉 Output:

Child method
🟨 3. Getting parent method using super()

If you still want parent method inside child:

class Parent:
    def show(self):
        print("Parent method")

class Child(Parent):
    def show(self):
        super().show()   # get parent method
        print("Child method")

c = Child()
c.show()

👉 Output:

Parent method
Child method
🟧 4. Direct parent class call

You can also call parent method explicitly:

class Parent:
    def show(self):
        print("Parent method")

class Child(Parent):
    def show(self):
        Parent.show(self)   # direct parent call
        print("Child method")

c = Child()
c.show()
🧠 IMPORTANT IDEA

👉 Methods are “inherited automatically”
👉 Python searches method using:

✔ MRO (Method Resolution Order)

Order:

Child → Parent → object
⚡ FINAL SUMMARY

You can get parent methods in 3 ways:

✔ Direct call → obj.method()
✔ super() → super().method()
✔ Parent class name → Parent.method(self)

🧠 Interview Answer:

In Python, parent class methods are accessed through inheritance. A child class can directly call inherited methods, override them if needed, or use super() 
to call the parent class method. Python resolves method calls using Method Resolution Order (MRO).

If you want next, I can explain:
✔ super() internal working (very important)
✔ MRO with multiple inheritance diagram
✔ tricky interview questions on method overriding
POLYMORPHISM:

give how static polymorphism and dynammic polymorphism achieved in python

In Python, polymorphism is mainly split into:

Static polymorphism (compile-time-like behavior)
Dynamic polymorphism (run-time behavior)

But important truth first:
👉 Python does not have real compile-time polymorphism like Java/C++
Instead, it simulates it using language features.

🟦 1. Static Polymorphism in Python (SIMULATED)
❗ Meaning:

Same function name, different behavior decided before runtime logic via arguments

Python achieves this using:

✔ Method overloading style (NOT real overloading)
✔ Default arguments
✔ *args / **kwargs
🔹 (A) Default arguments
class Calc:
    def add(self, a, b=0, c=0):
        return a + b + c

obj = Calc()
print(obj.add(10))
print(obj.add(10, 20))
print(obj.add(10, 20, 30))

👉 Behavior decided based on number of arguments (static-style dispatch)

🔹 (B) *args (most flexible static-style polymorphism)
class Calc:
    def add(self, *args):
        return sum(args)

obj = Calc()
print(obj.add(10, 20))
print(obj.add(10, 20, 30))

👉 Single method handles multiple “forms”

🧠 Key idea:

✔ Same method name
✔ Behavior changes based on parameters
❌ No runtime type decision like OOP inheritance

🟩 2. Dynamic Polymorphism in Python (REAL POLYMORPHISM)
❗ Meaning:

Same method name behaves differently based on object type at runtime

This is achieved using:

✔ Method Overriding
✔ Duck Typing
🔹 (A) Method Overriding (Inheritance-based)
class Animal:
    def sound(self):
        print("Generic sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")

animals = [Dog(), Cat(), Animal()]

for a in animals:
    a.sound()

👉 Same method, different class behavior (runtime decision)

🔹 (B) Duck Typing (Python’s strongest feature)
class Dog:
    def speak(self):
        print("Bark")

class Robot:
    def speak(self):
        print("Beep")

def make_sound(obj):
    obj.speak()   # runtime decision

make_sound(Dog())
make_sound(Robot())

👉 No inheritance required
👉 Only method matters

⚡ Key Difference Summary
Feature	Static Polymorphism	Dynamic Polymorphism
When decided	Before runtime (logic based on args)	During runtime
How achieved	default args, *args, **kwargs	method overriding, duck typing
Type dependency	No	Yes (behavior-based)
Flexibility	Medium	Very high
🧠 Interview-ready answer

In Python, static polymorphism is simulated using default arguments and *args to allow a single method to behave differently based on input parameters. Dynamic polymorphism is achieved through method overriding and duck typing, where the method to execute is decided at runtime based on the object type or behavior.

If you want, I can also give:

10 interview questions on polymorphism (very important for placements)
difference between polymorphism, inheritance, and abstraction (confusing topic)
real-world project example using both types together