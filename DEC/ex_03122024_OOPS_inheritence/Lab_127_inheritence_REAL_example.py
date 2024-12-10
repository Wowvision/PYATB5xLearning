class BaseTest:

    def Open_browser(self):
        print("Starting the browser")

    def close_Browser(self):
        print("Closing the browser")

    def read_from_excel_file(self):
        print("Read from excel")

class TestCase1(BaseTest):

    def test_Positive(self):
        self.Open_browser()
        print("Test case P1 executed")
        self.read_from_excel_file()
        self.close_Browser()

    def test_Negitive(self):
        self.Open_browser()
        print("Test case N1 executed")
        self.close_Browser()


class TestCase2(BaseTest):

    def test_Positive2(self):
        self.Open_browser()
        print("Test case P1 executed")
        self.close_Browser()

    def test_Negitive2(self):
        self.Open_browser()
        print("Test case N1 executed")
        self.close_Browser()

