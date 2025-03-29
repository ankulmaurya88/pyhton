
# Here discous about the Single Inheritance 
class Parent():
    def __init__(self):
        print("this is Single Inheritance ")

    def father(self):
        print("father is Farmer")


class Child(Parent):
    def __init__(self):
        super().__init__()  # Calls Parent's __init__()
        print("This is Child class")

    def item(self):
        print("I have good toys")



child=Child()

# print(child)




    