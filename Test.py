
class A:
    def method(self):
        print("Method in A")

class B(A):
    def method(self):
        print("Method in B")
        super().method() # Call next method in MRO

class C(A):
    def method(self):
        print("Method in C")
        super().method() # Call next method in MRO

class D(B, C):
    def method(self):
        print("Method in D")
        super().method() # Call next method in MRO

class E(C):
    def method(self):
        print("Method in E")
        super().method() # Call next method in MRO

class F(D, E):
    def method(self):
        print("Method in F")
        super().method() # Call next method in MRO


# Create an instance of F
f = F()
f.method()

# Print the MRO of class F
print("MRO of F:", F.mro())


"""
class A:
    def show(self):
        print("A's method")

class B(A):
    def show(self):
        super().show()
        print("B's method")
class C(A):
    def show(self):
        
        print("C's method")

class D(B, C):
    pass

d = D()
d.show()  # Method from B, as it is listed first in MRO. Print B's method only cuz no super()

# MRO for class D
print(D.__mro__)"""