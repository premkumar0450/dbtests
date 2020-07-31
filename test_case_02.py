import pytest

@pytest.mark.usefixtures("db_setup")
class Test_one:
    @pytest.fixture(autouse=True)
    def class_setup(self,db_setup):
        self.mydb= db_setup


    def test_02(self):
        print("second test")