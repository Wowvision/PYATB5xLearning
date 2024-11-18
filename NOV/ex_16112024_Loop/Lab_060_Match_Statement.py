# Write a program to ask which browser to run in automation

browser_name = input("Enter the browser name\n")

match browser_name:
    case "firefox":
        print("it is firfox browser")
    case "chrome":
        print("it is chrome browser")
    case "edge":
        print("it is edge browser browser")
    case "opera":
        print("it is opera browser")
    case _:
        print("Browser not found")
