from prettytable import PrettyTable
del_earnings = 0
class Student:
    
    def __init__(self, name, subject, avg_marks = [], days = 0, earnings = 0):
        self.name = name
        self.subject = subject
        self.avg_marks = avg_marks
        self.days = days
        self.earnings = earnings
    
    def add_student(self):
        record = []
        data = []
        subject = []
        avg_marks = []
        days = 0
        earnings = 0

        data.append(self.name)
        data.append(self.subject)
        data.append(avg_marks)
        data.append(self.days)
        data.append(self.earnings)
        return data

    def edit_student(record):
        edit_name = input("Enter the name of the student: ")
        for i in range(0, len(record)):  
            if edit_name == record[i][0]:
                new_days = int(input("Enter the number of days taught: "))
            
                new_earnings=0
                for j in range(0,len(record[i][1])):
                    if record[i][1][j] == 1:
                        new_earnings = new_earnings + 1

                marks = input("Enter the marks obtained by the student in recent exam: ")
                record[i][2].append(marks)
                record[i][3] = record[i][3] + new_days
                record[i][4] = record[i][4] + new_earnings * new_days
                print("----------------------")
                print("Student Data edited successfully")
                print("----------------------")
                return record
        else:
            print("Student record not found!!")
            return record

    def delete_student(record):
        temp_list = []
        del_earnings = 0
        del_name = input("Enter the name of the student to be deleted from record: ")

        for i in range(0, len(record)):
            if record[i][0] == del_name:
                del_earnings = del_earnings + record[i][4]
            else:
                temp_list.append(record[i])
    
        record = list(temp_list)

        return record, del_earnings

    def calc_avg_marks(record, index):
        sum_of_marks = 0

        if len(record[index][2][0]) == 0:
            average_marks = 0
            return average_marks 
        else:
            average_marks = 0
            for i in range(0, len(record[index][2])):
                sum_of_marks = sum_of_marks + int(record[index][2][i])
                average_marks = sum_of_marks / len(record[index][2])
            return average_marks
    
    def display_student(record):
        myTable = PrettyTable()
        myTable.field_names = ["SL no.", "Student Name", "Total Earnings", "Average Marks"]
        for i in range(0, len(record)):
            average_marks = Student.calc_avg_marks(record, i)
            myTable.add_row([str(i+1), record[i][0], record[i][4], average_marks])
    
        print(myTable)

        disp = input("Enter the SL no. of student whose details you want to view: ")

        average_marks = Student.calc_avg_marks(record, (int(disp)-1))
    
        if int(disp) <= ((len(record))+1):
            print("----------------------")
            print("Name: " + str(record[int(disp)-1][0]))
            print("Subjects: ")
            if record[int(disp)-1][1][0] == 1:
                print("Math")
            if record[int(disp)-1][1][1] == 1:
                print("English")
            if record[int(disp)-1][1][2] == 1:
                print("Bangla") 
            print("Average Marks Obtained: " + str(average_marks))
            print("Total Days Taught: " + str(record[int(disp)-1][3]))
            print("Total Earnings from this Student: " + str(record[int(disp)-1][4]))   
            print("----------------------")
            
        else:
            print("Enter a valid SL no.")

    def display_stats(record_class_8, record_class_9, record_class_10, del_earnings):
        print("----------------------")
  
        days_class_8 = 0
        days_class_9 = 0
        days_class_10 = 0
        earnings_class_8 = 0
        earnings_class_9 = 0
        earnings_class_10 = 0
        del_sum = 0
  
        for i in range(0, len(record_class_8)):
            days_class_8 = days_class_8 + record_class_8[i][3]
        for i in range(0, len(record_class_9)):
            days_class_9 = days_class_9 + record_class_9[i][3]
        for i in range(0, len(record_class_10)):
            days_class_10 = days_class_10 + record_class_10[i][3]

        total_days = days_class_8 + days_class_9 + days_class_10
        print("Total days taught across all classes: " + str(total_days))
        print("Total days taught in class 8: " + str(days_class_8))
        print("Total days taught in class 9: " + str(days_class_9))
        print("Total days taught in class 10: " + str(days_class_10))

        for i in range(0, len(record_class_8)):
            earnings_class_8 = earnings_class_8 + record_class_8[i][4]
        for i in range(0, len(record_class_9)):
            earnings_class_9 = earnings_class_9 + record_class_9[i][4]
        for i in range(0, len(record_class_10)):
            earnings_class_10 = earnings_class_10 + record_class_10[i][4]

        for i in range(0, len(del_earnings)):
            del_sum = del_sum + del_earnings[i] 

        total_earnings = earnings_class_8 + earnings_class_9 + earnings_class_10 + del_sum
        print("Total earnings across all classes: " + str(total_earnings))
        print("Total earnings in class 8: " + str(earnings_class_8))
        print("Total earnings in class 9: " + str(earnings_class_9))
        print("Total earnings in class 10: " + str(earnings_class_10))

        #Individual earning of each subject
        earning_math_8 = 0
        earning_english_8 = 0
        earning_bangla_8 = 0

        earning_math_9 = 0
        earning_english_9 = 0
        earning_bangla_9 = 0

        earning_math_10 = 0
        earning_english_10 = 0
        earning_bangla_10 = 0

        for i in range(0, len(record_class_8)):
            if record_class_8[i][1][0] == 1:
                earning_math_8 = earning_math_8 + (1 * record_class_8[i][3])
            if record_class_8[i][1][1] == 1:
                earning_english_8 = earning_english_8 + (1 * record_class_8[i][3])
            if record_class_8[i][1][2] == 1:
                earning_bangla_8 = earning_bangla_8 + (1 * record_class_8[i][3])
        
        for i in range(0, len(record_class_9)):
            if record_class_9[i][1][0] == 1:
                earning_math_9 = earning_math_9 + (1 * record_class_9[i][3])
            if record_class_9[i][1][1] == 1:
                earning_english_9 = earning_english_9 + (1 * record_class_9[i][3])
            if record_class_9[i][1][2] == 1:
                earning_bangla_9 = earning_bangla_9 + (1 * record_class_9[i][3])
        
        for i in range(0, len(record_class_10)):
            if record_class_10[i][1][0] == 1:
                earning_math_10 = earning_math_10 + (1 * record_class_10[i][3])
            if record_class_10[i][1][1] == 1:
                earning_english_10 = earning_english_10 + (1 * record_class_10[i][3])
            if record_class_10[i][1][2] == 1:
                earning_bangla_10 = earning_bangla_10 + (1 * record_class_10[i][3])

        total_earnings_math = earning_math_8 + earning_math_9 + earning_math_10
        total_earnings_english = earning_english_8 + earning_english_9 + earning_english_10
        total_earnings_bangla = earning_bangla_8 + earning_bangla_9 + earning_bangla_10

        print("Total earnings from teaching Math: " + str(total_earnings_math))
        print("Total earnings from teaching English: " + str(total_earnings_english))
        print("Total earnings from teaching Bangla: " + str(total_earnings_bangla))
        
        average_marks_8 = 0
        average_marks_9 = 0
        average_marks_10 = 0

        for i in range(0, len(record_class_8)):
            marks_individual_8 = 0
            for j in range(0, len(record_class_8[i][2])):
                marks_individual_8 = marks_individual_8 + int(record_class_8[i][2][j])
            marks_individual_8 = marks_individual_8 / len(record_class_8[i][2])
            average_marks_8 = average_marks_8 + marks_individual_8

        for i in range(0, len(record_class_9)):
            marks_individual_9 = 0
            for j in range(0, len(record_class_9[i][2])):
                marks_individual_9 = marks_individual_9 + int(record_class_9[i][2][j])
            marks_individual_9 = marks_individual_9 / len(record_class_9[i][2])
            average_marks_9 = average_marks_9 + marks_individual_9

        for i in range(0, len(record_class_10)):
            marks_individual_10 = 0
            for j in range(0, len(record_class_10[i][2])):
                marks_individual_10 = marks_individual_10 + int(record_class_10[i][2][j])
            marks_individual_10 = marks_individual_10 / len(record_class_10[i][2])
            average_marks_10 = average_marks_10 + marks_individual_10

        if len(record_class_8) > 0:
            average_marks_8 = average_marks_8 / len(record_class_8)
        else:
            average_marks_8 = 0
        if len(record_class_9) > 0:
            average_marks_9 = average_marks_9 / len(record_class_9)
        else:
            average_marks_9 = 0
        if len(record_class_10) > 0:
            average_marks_10 = average_marks_10 / len(record_class_10)
        else:
            average_marks_10 = 0

        total_average_marks = (average_marks_8 + average_marks_9 + average_marks_10) / 3
        print("Average marks across all classes: " + str(total_average_marks))
        print("Average marks in class 8: " + str(average_marks_8))
        print("Average marks in class 9: " + str(average_marks_9))
        print("Average marks in class 10: " + str(average_marks_10))
        
        print("----------------------")