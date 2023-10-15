
class User:

    x = 10

    def __init__(self, initialValue): # It is used to initialize some values when creating a new object.
        # Initialize attributes/variables 
        self.name = initialValue

    def greet(self):
        self.name = "user_1"
        self.x = 40
        print(f"Hello {self.name}")

    




user_1 = User("Timmy")
user_1.greet()
print(user_1.x)


user_2 = User("Varun")
user_2.greet()
print(user_2.name)