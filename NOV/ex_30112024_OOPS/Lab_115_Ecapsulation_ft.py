# Web Automation-Selenium
# Page-You arte going to automate
from dotenv import load_dotenv
import os


class VWOLoginPage:

    def __init__(self, email_arg, password_arg):

        self.email = email_arg
        self.password = password_arg

    def login_confirm(self):
        if self.email == "pramod@gmail.com" and self.password == "Pass123":
            print("Allowed , Login success")
        else:
            print("Login failed")

load_dotenv()

email = os.getenv("EMAIL")# Read from test data - excel,csv file or env file
password = os.getenv("PASSWORD")# Read from test data - excel,csv file or env file

print(email, password)

object_ref = VWOLoginPage(email,password)
object_ref.login_confirm()

