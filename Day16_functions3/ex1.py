def outter():

    def inner():
        print('Inner function')

    print('outter function')
    inner()

outter()

