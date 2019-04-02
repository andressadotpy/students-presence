import unittest
from students import Students

class TestingStudents(unittest.TestCase):

    def test_is_returning_full_name(self):
        a = Students("FirstName", "LastName", "X", "X")
        assert a.full_name() == "FirstName LastName", "Is not returning full name."

    def test_is_returning_right_data_format(self):
        a = Students("FirstName", "LastName", "X", "X")
        assert a.student_presence(0) == [('2019-04-02', 0)], "Is not returning list of tuple."

    # test is returning right csv file name to second year
    def test_is_returning_right_file1(self):
        a = Students("FirstName", "LastName", "2", "Morning")
        assert a.student_right_file() == "Students_presence_2_3.csv", "Is not returning right file."

    # test is returning right csv file name to third year
    def test_is_returning_right_file2(self):
        a = Students("FirstName", "LastName", "3", "Morning")
        assert a.student_right_file() == "Students_presence_2_3.csv", "Is not returning right file."

    # test is returning right csv file name to 4th year morning shift
    def test_is_returning_right_file3(self):
        a = Students("FirstName", "LastName", "4", "Morning")
        assert a.student_right_file() == "Students_presence_4_5.csv", "Is not returning right file."

    # test is returning right csv file name to 5th year morning shift
    def test_is_returning_right_file4(self):
        a = Students("FirstName", "LastName", "5", "Morning")
        assert a.student_right_file() == "Students_presence_4_5.csv", "Is not returning right file."

    # test is returning right csv file name to 4th year afternoon shift
    def test_is_returning_right_file6(self):
        a = Students("FirstName", "LastName", "4", "Afternoon")
        assert a.student_right_file() == "Students_presence_4_5_6.csv", "Is not returning right file."

    # test is returning right csv file to 5th year afternoon shift
    def test_is_returning_right_file7(self):
        a = Students("FirstName", "LastName", "5", "Afternoon")
        assert a.student_right_file() == "Students_presence_4_5_6.csv", "Is not returning right file."

    # test is returning right csv file to 6th year
    def test_is_returning_right_file8(self):
        a = Students("FirstName", "LastName", "6", "Afternoon")
        assert a.student_right_file() == "Students_presence_4_5_6.csv", "Is not returning right file."
