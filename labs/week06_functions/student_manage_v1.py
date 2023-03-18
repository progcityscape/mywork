# this is a program to manage student data from a number of students, building on week 05
# author John Kelleher

# Write a function that prints out a menu of commands we can perform, ie add,
# view and quit. The function should return what the user chose.

# # import code from student_manage_v1x.py where we tested the code
# import student_manage_v1x

# store a simple Dict to a file as JSON.

import json

FILENAME = "testdict.json"
sample = dict(name='Fred', age=31, grades = [1,3,4,55])

def write_dict(obj):
    with open (FILENAME, 'wt') as f:
        json.dump(obj,f)

def display_menu ():
    print ("What would you like to do?")
    print ("\t(a) Add new student")
    print ("\t(v) View students")
    print ("\t(s) Save students")
    print ("\t(q) Quit")
    choice = input("Type one letter (a/v/s/q): ").strip ()

    return choice

# # test the function
# choice = display_menu()

# print (f"You chose {choice}")

# create an empty list
# students = []
# empty function to be created later will return a list

def do_add (students):
    current_student = {}
    # add a name to the student dictionary via user input
    current_student ["name"] = input ("enter name :")
    # populate 'modules' via as yet undefined function
    current_student ["modules"] = read_modules ()
    # add the dictionary to the 'students' argument/variable
    students.append (current_student)

# now add this code to student_manage_v1.py (I'll try this via import)


def read_modules ():
    # read in a module name
    modules = []
    module_name = input("Enter the first module name (blank to quit):").strip ()

    # create a loop to repeat the process until blank is entered
    while module_name != "":
        # create a dictionary containing module name and grade
        module = {}
        module["name"] = module_name
        # no error handling for the moment
        module["grade"] = int(input("\t\tEnter grade:"))
        # similar to do_add but apending within the scope of the function
        modules.append(module)
        # now read next module name
        # this is basically the same code as the 1st block (line (this minus 12))
        # could this be a function as well?
        module_name = input("\tEnter the next module name (blank to quit):").strip ()


    return modules


    # def doAdd():
    #  # we fill this in later
    #  print("in adding")

# create the do_add process using two functions

def display_modules (modules):
    print ("\tName  \tGrade")
    for module in modules:
        print (f"\t{module['Name']} \t{module['Grade']}")

def do_view(students):
    for current_student in students:
        print (current_student["name"])
        display_modules(current_student["modules"]);

def do_save(students):
    write_dict (students)
    print ("Students Saved.")
    print ("in save")
     

# main program
students = []
choice = display_menu ()

while (choice != 'q'):
    if choice == 'a':
        do_add(students)
    elif choice == 'v':
        do_view(students)
    elif choice == 's':
        do_save(students)
    elif choice != 'q':
        print ("\n\n Please select either a,v,s or q")
    choice = display_menu ()



