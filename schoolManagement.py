listt = {}
teacher_list = {}

def readTechers():
    with open("tData.txt","r") as f:
        for line in f:
            name,stream,specialist,hod = line.strip().split(",")
            teacher_list[name] = [stream,specialist,hod] 


def writeTeachers(self,name,stream,specialist,hod):
    with open("tData.txt","a") as f:
        f.write(f"{name},{stream},{specialist},{hod}\n")

def readData():
    with open("sMD.txt", "r") as f:
        for line in f:
            name, student_id, roll,stream, stu_id = line.strip().split(",")
            listt[name] = [student_id, roll, stream, stu_id]

def writeData(name, student_id, roll,stream,stu_num):
    with open("sMD.txt", "a") as f:
        f.write(f"{name},{student_id},{roll},{stream},{stu_num}\n")


# Read data before creating a new student
readData()

class Student:
    global listt
    # Initialize from existing data if available, otherwise start from default values
    student_number = int(listt[list(listt.keys())[-1]][3]) if listt else 0  # From last student's stu_id
    roll = int(listt[list(listt.keys())[-1]][1]) if listt else 0  # From last student's roll number
    id = int(listt[list(listt.keys())[-1]][0]) if listt else 2810012100  # From last student's id or default

    def __init__(self, name,stream):
        self.name = name
        self.stream = stream
        self.id = Student.id + 1
        self.roll = Student.roll + 1
        Student.student_number += 1
        Student.roll += 1
        Student.id += 1

        writeData(self.name, self.id, self.roll,self.stream, Student.student_number)

    def welcome(self):
        print(f"Welcome {self.name} You are now a student Of Our School \nRoll No = {self.roll}\nStudent Id = {self.id}\nStudy Hard!")




class Teacher:
    teacher_count = 0
    teacher_id = 0

    def __init__(self,name,stream,specialist,hod = False):
        self.name = name
        self.stream = stream
        self.specialist = specialist
        self.hod = hod
        Teacher.teacher_count += 1
        Teacher.teacher_id += 1 

        writeTeachers(self,self.name,self.stream,self.specialist,self.hod)


    def welcome(self):
        print("Welcome Prof {name}. You are now our{self.specialist} teacher And Your Department is {self.stream}")
    


# Create a new student after reading data


# Print all student names after adding the new student
print(f"Total Number Of Student In College:-{Student.student_number}")
for name, details in listt.items():
    id,roll,stream,count = details
    print(f"Name :- {name}\t Roll No :- {roll}\nStream = {stream}")

kundu = Teacher("Debasis Kundu","Science","Physics",True)











