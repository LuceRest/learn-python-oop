class A:

    def method_A(self):
        print("Ini adalah method A")


class B:
    
    def method_B(self):
        print("Ini adalah method B")


class C(A,B):
    pass


objek = C()

print()
objek.method_A()

print()

objek.method_B()
print()



'''
    NB :
        - Multiple inheritance	-> Subclass dapat mewarisi method-method dari dua atau lebih superclass.

        - Mutiple inheritance di python :
            class <nama subclass>(<nama superclass 1>, <nama superclass 2>):
                <action>


'''


        