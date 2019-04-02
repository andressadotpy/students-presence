from students import Students
import csv
import operator

class Files():

    def __init__(self, file):
        self.file = file

    def open_file(self):
        with open(self.file, "r", encoding = "utf-8") as students_data:
            lines = students_data.readlines()
        for row in lines:
            print(lines)

    def append_in_file(self, new_student_data):
        self.new_student_data = new_student_data
        with open(self.file, "a", encoding = "utf-8", newline = "") as students_data:
            f = csv.writer(students_data, delimiter = ",")
            f.writerow(self.new_student_data)

    def organizing_students_files(self):
        data = csv.reader(open(self.file, newline=''), delimiter=',')
        sortedlist= sorted(data, key=operator.itemgetter(0))
        with open(self.file, 'w', newline='') as f:
            f_writer = csv.writer(f, delimiter= ',')
            for row in sortedlist:
                f_writer.writerow(row)
