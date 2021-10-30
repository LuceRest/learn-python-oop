# Method Resolution Order

class A:
    
    def show(self):
        print("Ini adalah show A")


class B:

    def show(self):
        print("Ini adalah show B")


class C(B,A):
    pass


objek = C()
objek.show()
# help(objek)



'''
    NB :
        - Method resolution order	-> Urutan method yg akan dijalankan apabila nama methodnya sama.
        - class subclass(<superclass 1>, superclass 2>)	=> Method resolutionnya yaitu subclass, superclass 1, superclass 2.


'''


