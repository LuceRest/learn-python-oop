# Membuat Class Abstract
# abc = abstract base class

from abc import ABC, abstractmethod

class Button(ABC):

    @abstractmethod
    def click(self):
        pass


class PushButton(Button):
    
    def click(self):
        print("Push button click")


class RadioButton(Button):

    def click(self):
        print("Radio button click")


tombol1 = PushButton()
tombol2 = RadioButton()
    
tombol1.click()
tombol2.click()
    


'''
    NB :
        - Class abctract	~> Berfungsi untuk memaksa suatu class untuk menggunakan method-method dari class abstract tersebut.
        - Class abstract di python :
            class <nama class abstract>(ABC):
                @abstractmethod
                def <nama method abstract>():
                    <action>


'''

