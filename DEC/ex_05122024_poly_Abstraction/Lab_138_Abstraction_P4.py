from abc import ABC, abstractmethod

class ExcelReader:

    @abstractmethod
    def read_from_excel(self):
        pass

class Browser(ExcelReader):

    @abstractmethod
    def start_browser(self):
        pass

    @abstractmethod
    def stop_browser(self):
        pass

class TC1(Browser):

    def start_browser(self):
        print("Starting")

    def stop_browser(self):
        print("Stoping")

    def read_from_excel(self):
        print("readfromexcel is ready")

    def runTC1(self):
        self.start_browser()
        self.read_from_excel()
        self.stop_browser()

tc_ref = TC1()
tc_ref.runTC1()


