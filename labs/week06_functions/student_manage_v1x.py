# offshoot to test function for reading in students

# create an empty list
students = []
# empty function to be created later will return a list
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

def do_add (students):
    current_student = {}
    # add a name to the student dictionary via user input
    current_student ["name"] = input ("enter name :")
    # populate 'modules' via as yet undefined function
    current_student ["modules"] = read_modules ()
    # add the dictionary to the 'students' argument/variable
    students.append (current_student)

# now add this code to student_manage_v1.py (I'll try this via import)
    

# test
do_add (students)

do_add (students)
print (students)

# now create function to read in modules



