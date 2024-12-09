# Web Automation-Selenium
# Page-You arte going to automate


class VWOLoginPage:

    def __init__(self, email_arg, password_arg):

        self.email = email_arg
        self.password = password_arg

    def login_confirm(self):
        if self.email == "pramod@gmail.com" and self.password == "Pass123":
            print("Allowed , Login success")
        else:
            print("Login failed")

# email = input("Enter the email \n")
# password = input("Enter the password \n")

# object_ref = VWOLoginPage(email,password)
# object_ref.login_confirm()

pramod = VWOLoginPage("pramod@gmail.com","Pass123")
pramod.login_confirm()