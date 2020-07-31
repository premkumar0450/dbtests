import pytest
from ddt import ddt, data, unpack
from read_data import getCSVData
import unittest

@pytest.mark.usefixtures("db_setup")
@ddt
class Test_one(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def class_setup(self,db_setup):
        self.mydb= db_setup

    @data(*getCSVData("query.csv"))
    @unpack
    def test_01(self,query):
        cursor = self.mydb.cursor()
        cursor.execute(query)
        record = cursor.fetchall()
        print(record)