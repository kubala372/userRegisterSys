class Register:
    def __init__(self):
        self.username = input("Enter your username: ")
        self.password = input("Enter your password: ")
        self.passwordConfirm = input("Confirm your password: ")

    def test(self):
        if self.username == "":
            print("the username field is empty")
        elif self.password == "" or self.passwordConfirm == "":
            print("a password must be entered or confirmed")
        elif self.password != self.passwordConfirm:
            print("your password doesn't match")


obj1 = Register()
obj1.test()
