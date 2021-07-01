from student import Student,del_earnings
from goto import with_goto
import pickle

record_class_8 = []                
record_class_9 = []
record_class_10 = []
del_earnings = []


with open("record_class_8.txt", "rb") as fp:
    while 1:
        try:
            record_class_8 = pickle.load(fp)
#             print(record_class_8)
        except EOFError:
            break
with open("record_class_9.txt", "rb") as fp:
     while 1:
        try:
            record_class_9 = pickle.load(fp)
#             print(record_class_9)
        except EOFError:
            break
with open("record_class_10.txt", "rb") as fp:
    while 1:
        try:
            record_class_10 = pickle.load(fp)
#             print(record_class_10)
        except EOFError:
            break
with open("del_earnings.txt", "rb") as fp:
    while 1:
        try:
            del_earnings = pickle.load(fp)
#             print(del_earnings)
        except EOFError:
            break

print ("Enter 1 to add a record of student of class 8")
print ("Enter 2 to add a record of student of class 9")
print ("Enter 3 to add a record of student of class 10")
if len(record_class_8) >= 1:
    print ("Enter 4 to display the overall info")
print ("Enter 5 to End program")

x = int(input("Enter your choice: "))

if x == 1:
    while True:
        print("Enter 1 to Create new student record")
  
        if len(record_class_8) >= 1:                                   
            print("Enter 2 to Edit a student record")
  
        if len(record_class_8) >= 1:
            print("Enter 3 to Delete a student record")

        if len(record_class_8) >= 1: 
            print("Enter 4 to Display student records")

        if len(record_class_8) >= 1: 
            print("Enter 5 to Display the overall info")

        print("Enter 6 to End program")

  
        i = input("Enter your choice: ")                                   

        if int(i) == 1:
            subject = []
            temp_list = []
            name = input("Enter the name of student: ")
            print("Enter '1' for subjects you teach among Math, Engish and Bangla and '0' for those you do not sequentially: ")
            try:
                math = int(input("Math: "))
                english = int(input("English: "))
                bangla = int(input("Bangla: "))
                if math < 0 or math > 1 or english < 0 or english > 1 or bangla < 0 or bangla > 1:
                    raise ValueError
            except ValueError:
                print("Invalid input. The input must be 1 or 0!!")
                break
            
            subject.extend([math, english, bangla])
            student = Student(name, subject)
            temp_list = student.add_student()
            record_class_8.append(temp_list)
            # print(record_class_8)
            with open("record_class_8.txt", "wb") as fp:
                pickle.dump(record_class_8,fp)

        elif int(i)==2:
            record_class_8 = Student.edit_student(record_class_8)
            with open("record_class_8.txt", "wb") as fp:
                pickle.dump(record_class_8,fp)     
            
        elif int(i)==3:
            tempo = 0
            record_class_8, tempo = Student.delete_student(record_class_8)
            del_earnings.append(tempo)

            with open("record_class_8.txt", "wb") as fp:
                pickle.dump(record_class_8,fp)
            with open("del_earnings.txt", "wb") as fp:
                pickle.dump(del_earnings,fp)                       
                                      
        elif int(i)==4:
            Student.display_student(record_class_8)

        elif int(i)==5:
            Student.display_stats(record_class_8, record_class_9, record_class_10, del_earnings)                     

        elif int(i)==6:
            break

        # elif int(i)==7:
        #     print(record_class_8)                         
        
        else:
            print("Invalid Choice, Try again!")

if x == 2:
    while True:                                                    
        print("Enter 1 to Create new student record")
  
        if len(record_class_9) >= 1:                                   
            print("Enter 2 to Edit a student record")
  
        if len(record_class_9) >= 1:
            print("Enter 3 to Delete a student record")

        if len(record_class_9) >= 1: 
            print("Enter 4 to Display student records")

        if len(record_class_9) >= 1: 
            print("Enter 5 to Display the overall info")

        print("Enter 6 to End program")

  
        i = input("Enter your choice: ")                                   

        if int(i) == 1:
            subject = []
            temp_list = []
            name = input("Enter the name of student: ")
            print("Enter '1' for subjects you teach among Math, Engish and Bangla and '0' for those you do not sequentially: ")
            math = int(input("Math: "))
            english = int(input("English: "))
            bangla = int(input("Bangla: "))
            subject.extend([math, english, bangla])
            student = Student(name, subject)
            temp_list = student.add_student()
            record_class_9.append(temp_list)
            with open("record_class_9.txt", "wb") as fp:
                pickle.dump(record_class_9,fp)

        elif int(i)==2:
            record_class_9 = Student.edit_student(record_class_9)
            with open("record_class_9.txt", "wb") as fp:
                pickle.dump(record_class_9,fp)   

        elif int(i)==3:
            tempo = 0
            record_class_9, tempo = Student.delete_student(record_class_9)
            del_earnings.append(tempo)

            with open("record_class_9.txt", "wb") as fp:
                pickle.dump(record_class_9,fp)
            with open("del_earnings.txt", "wb") as fp:
                pickle.dump(del_earnings,fp)                       
                                  
        elif int(i)==4:
            Student.display_student(record_class_9)

        elif int(i)==5:
            Student.display_stats(record_class_8, record_class_9, record_class_10, del_earnings)                     

        elif int(i)==6:
            break

        # elif int(i)==7:
        #     print(record_class_9)                         
        
        else:
            print("Invalid Choice, Try again!")

if x == 3:
    while True:                                                    
        print("Enter 1 to Create new student record")
  
        if len(record_class_10) >= 1:                                   
            print("Enter 2 to Edit a student record")
  
        if len(record_class_10) >= 1:
            print("Enter 3 to Delete a student record")

        if len(record_class_10) >= 1: 
            print("Enter 4 to Display student records")

        if len(record_class_10) >= 1: 
            print("Enter 5 to Display the overall info")

        print("Enter 6 to End program")

  
        i = input("Enter your choice: ")                                   

        if int(i) == 1:
            subject = []
            temp_list = []
            name = input("Enter the name of student: ")
            print("Enter '1' for subjects you teach among Math, Engish and Bangla and '0' for those you do not sequentially: ")
            math = int(input("Math: "))
            english = int(input("English: "))
            bangla = int(input("Bangla: "))
            subject.extend([math, english, bangla])
            student = Student(name, subject)
            temp_list = student.add_student()
            record_class_10.append(temp_list)
            with open("record_class_10.txt", "wb") as fp:
                pickle.dump(record_class_10,fp)

        elif int(i)==2:
            record_class_10 = Student.edit_student(record_class_10)
            with open("record_class_10.txt", "wb") as fp:
                pickle.dump(record_class_10,fp)   
        
        elif int(i)==3:
            tempo = 0
            record_class_10, tempo = Student.delete_student(record_class_10)
            del_earnings.append(tempo)

            with open("record_class_10.txt", "wb") as fp:
                pickle.dump(record_class_10,fp)
            with open("del_earnings.txt", "wb") as fp:
                pickle.dump(del_earnings,fp)                       
                               
        elif int(i)==4:
            Student.display_student(record_class_10)

        elif int(i)==5:
            Student.display_stats(record_class_8, record_class_9, record_class_10, del_earnings)                     

        elif int(i)==6:
            break

        # elif int(i)==7:
        #     print(record_class_10)                         
        
        else:
            print("Invalid Choice, Try again!")

if x==4:
    Student.display_stats(record_class_8, record_class_9, record_class_10, del_earnings)

if x==5:
    quit()
