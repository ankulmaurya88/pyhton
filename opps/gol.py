global_var = "Python is awesome!"

class MyClass:
    @staticmethod
    def print_global():
        global global_var
        print(global_var)  

MyClass.print_global()
