# a program that stores a student name and a list of her courses and grades in a dict, the program should then print out her data.
# author: John Kelleher

# student = {
#     "name":"Mary",
#     "modules": [
#         {
#             "course_name":"programming",
#             "grade": 45
#         },
#         {
#             "course_name":"history",
#             "grade": 99

#         }
        
#     ]
# }

# print ("Student: {}".format(student["name"]))

# for module in student ["modules"]:
#     print ("\t {} \t: {}".format(module["course_name"], module["grade"]))

# student_you = input("What is your name?:")

# module_dict = {}



# create a dictionary for the module names
# https://www.guru99.com/python-dictionary-append.html - to append to dictionary

student_name = input("What is your name?:")
module_list = {"Module Name: ": []}

# create a function to read input from the user and check if it is blank
# https://stackoverflow.com/questions/41026417/prompting-for-input-until-2-blank-lines-are-given - for number of empty responses code
# https://www.toolsqa.com/python/python-while-loop/ - for while True loop


def module_input ():
    
    # open a counter variable
    number_of_empty_responses = 0
    # check while loop against a counter
    while number_of_empty_responses == 0:
        module = input("Please enter the module name: ")
        if module != "":
            number_of_empty_responses = 0 
        
            module_list ["Module Name: "].append(module) 
            print (module_list)
        else:
            number_of_empty_responses += 1
            
            
# functional but presentation could be better
# also could add grades to the dictionary
    
module_input ()
print (f"Student Name: {student_name} {module_list}")





    
        










