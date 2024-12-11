class Old_Browser:

    def open_browser(self):
        print("IE is opening")

    def close_browser(self):
        print("IE is closing")

class Chrome(Old_Browser):


    def open_browser(self):
        super().open_browser()   #parent open browser also
        print("Better chrome browser is staring")

    def close_browser(self):
        print("Better chrome browser is stoping")

chrome_ref = Chrome()
chrome_ref.open_browser()
chrome_ref.close_browser()