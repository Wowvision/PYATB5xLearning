from browser_package.OpenBrowser import start_browser
from browser_package.CloseBrowser import stop_browser



# start_browser()
# print("Hello")
# stop_browser()

#this can be created within function
# def test_Case():
#     start_browser()
#     print("Hello")
#     stop_browser()
# test_Case()

#using the class
class test_case():
    def test_Case(self):
        start_browser()
        print("Hello")
        stop_browser()
testcase_obj = test_case()
testcase_obj.test_Case()
