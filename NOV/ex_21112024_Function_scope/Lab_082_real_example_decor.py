import time
def time_decorator(func):
    def wrapper():
        start_time = time.time()
        print(start_time)
        func()
        end_time = time.time()
        print(end_time)
        print("Total time taken by function _>", end_time-start_time)
    return wrapper()

def new_ui(func1):
    def wrapper():
        print("start")
        func1()
        print("stop")
    return wrapper()

@new_ui
@time_decorator
def test_ui1():
    print("Add a function , time taken by this function")
    time.sleep(3)


@time_decorator
def test_ui2():
    print("Add a function, time taken by this function")
    time.sleep(5)