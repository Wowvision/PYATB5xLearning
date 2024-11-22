def before_test_after_test(func):
    def before():
        print("Before the running UI TC")
        print("Launch browser")
        func()
        print("Ending the running tc")
        print("Quit browser")


    return before()




@before_test_after_test
def test_ui():
    print("I will test the UI")