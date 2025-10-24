class parent:
    def __init__(self):
        pass
    def show(self):
        print('Parent method')

class child(parent):
    def __init__(self):
        super().__init__()

    def show(self):
        super().show()
        print('child method')    

c=child()
c.show()            