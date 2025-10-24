from abc import ABC,abstractmethod


class parent(ABC):
    def __init__(self):
        pass
    def show(self):
        print('Parent class')
    @abstractmethod
    def display(self):
        pass

class child(parent):
    def __init__(self):
        super().__init__()
    def display(self):
        print('Child class')


C=child()
C.display()
C.show()                    