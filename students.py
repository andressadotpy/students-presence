#! /usr/bin/python3
# ChallengerSchoolStudents.py - A program to manage students presence at the "Strategy Games" classes.
from datetime import date
import sys

class Students():
    """Manage students of Challenger School at Marista Santa Maria.
    This is valid only for students of the "Strategy Games" class."""

    student_data = []
    students_local = "Challenger School"
    officine = "Strategy Games"

    def __init__(self, first_name, last_name, student_class, shift):
        self.first_name = first_name
        self.last_name = last_name
        self.student_class = student_class
        self.shift = shift

    def full_name(self):
        """ Method concatenates strings using the + operator.
        Returns student's full name."""
        return str(self.first_name + " " + self.last_name)

    def student_presence(self, present):
        """Method gets date of class day and if student was present.
        Present student = 1 and Not Present = 0.
        After, the method returns a list of tuple formated as [(date, presence)]"""

        dt = date.today()
        dt2 = format(dt)
        Students.student_data.append((dt2, present))
        return Students.student_data

    def student_right_file(self):

        # 2nd and 3rd years it's only on morning shift
        if ((self.student_class == "2") | (self.student_class == "3")):
            return "Students_presence_2_3.csv"

        # 4th and 5th years can be morning shift or afternoon shift
        elif (((self.student_class == "4") | (self.student_class == "5")) & (self.shift == "Morning")):
            return "Students_presence_4_5.csv"

        # 6th year it's only afternoon shift
        elif ((self.student_class == "6") | (((self.student_class == "4") | (self.student_class == "5")) & (self.shift == "Afternoon"))):
            return "Students_presence_4_5_6.csv"
