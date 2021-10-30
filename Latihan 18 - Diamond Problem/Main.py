# Diamond Problem

class A:
    
    def show(self):
        print("Ini adalah show A")


class B(A):
    
    def show(self):
        print("Ini adalah show B")


class C(A):
    
    def show(self):
        print("Ini adalah show C")


class D(B,C):
    pass


objek = D()
objek.show()



'''
    NB :
        - class <subclass terkecil>(<subclass 1>, subclass 2>)	=> Method resolutionnya yaitu subclass terkecil, subclass 1, subclass 2, superclass.


'''

