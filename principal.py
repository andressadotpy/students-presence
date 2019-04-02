while True:
    OPERATION = ['1 : Add new student',
                 '2: Organize students files',
                 '3: End program']
    print(OPERATION)
    choice = input('Type operation: \n')

    if (choice == '1'):
        first_name_std = input('Student first name: ')
        last_name_std = input('Student last name: ')
        class_std = input('Student class: ')
        std = Students(first_name_std, last_name_std, class_std)
        a = std.student_classes()
        if (a == 1):
            p = input('Present = 1 Not present = 0: ')
            f1 = open('Students_presence_2_3.csv', 'a', newline='')
            csv_f1_writer = csv.writer(f1, delimiter=',')
            csv_f1_writer.writerow([std.full_name(), class_std, std.student_presence(p)])
            f1.close()
        elif (a == 2):
            p = input('Present = 1 Not present = 0: ')
            f2 = open('Students_presence_4_5.csv', 'a', newline='')
            csv_f2_writer = csv.writer(f2, delimiter= ',')
            csv_f2_writer.writerow([std.full_name(), class_std, std.student_presence(p)])
            f2.close()
        elif (a == 3) | (a == 4):
            p = input('Present = 1 Not present = 0: ')
            f3 = open('Students_presence_4_5_6.csv', 'a', newline='')
            csv_f3_writer = csv.writer(f3, delimiter=',')
            csv_f3_writer.writerow([std.full_name(), class_std, std.student_presence(p)])
            f3.close()
    if (choice == '2'):


        data = csv.reader(open('Students_presence_2_3.csv', newline=''), delimiter=',')
        sortedlist= sorted(data, key=operator.itemgetter(0))
        with open('Students_presence_2_3.csv', 'w', newline='') as f:
            f_writer = csv.writer(f, delimiter= ',')
            for row in sortedlist:
                f_writer.writerow(row)

        data = csv.reader(open('Students_presence_4_5.csv', newline=''), delimiter=',')
        sortedlist= sorted(data, key=operator.itemgetter(0))
        with open('Students_presence_4_5.csv', 'w', newline='') as f:
            f_writer = csv.writer(f, delimiter= ',')
            for row in sortedlist:
                f_writer.writerow(row)

        data = csv.reader(open('Students_presence_4_5_6.csv', newline=''), delimiter=',')
        sortedlist= sorted(data, key=operator.itemgetter(0))
        with open('Students_presence_4_5_6.csv', 'w', newline='') as f:
            f_writer = csv.writer(f, delimiter= ',')
            for row in sortedlist:
                f_writer.writerow(row)

    elif (choice == '3'):
        break
    else:
        raise Exception("{} is not a valid entry.".format(choice))
