#
#
# class A:
#     _value = 10
#
#     def method(self):
#         #code for A version
#         pass
#
# class B(A):
#     _value = 20
#
#     def method(self):
#         #code for B version
#         pass
#
# class C(A):
#     _value = 30
#
#     def method(self):
#         #code for C version
#         pass
#
# class D(C, B):
#     pass

# C3 Linearization Algorithm

class X:pass
class Y:pass
class Z:pass
class A(X,Y):pass
class B(Y,Z):pass
class M(B,A,Z):pass

print(M.mro())















