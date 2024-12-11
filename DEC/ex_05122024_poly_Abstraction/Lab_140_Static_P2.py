class Excel_reader:

    @staticmethod
    def read_from_excel():
        print("Reading from excel")

class MYSQLFunction:

    @staticmethod
    def read_my_sql_file():
        print("SQL")

class TC1:

    def testcase(self):
        Excel_reader.read_from_excel()
        MYSQLFunction.read_my_sql_file()


tc_ref = TC1()
tc_ref.testcase()
