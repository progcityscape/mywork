# a program that stores a student name and a list of her courses and grades in a dict, the program should then print out her data.
# author: John Kelleher

student = {
    "name":"Mary",
    "modules": [
        {
            "course_name":"programming",
            "grade": 45
        },
        {
            "course_name":"history",
            "grade": 99

        }
        
    ]
}

print ("Student: {}".format(student["name"]))

for module in student ["modules"]:
    print ("\t {} \t: {}".format(module["course_name"], module["grade"]))