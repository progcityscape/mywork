#addOneExtension.py
#this program reads a number and adds one to get a bigger number
#it is limited to numbers between 0 and 10

#for loop to extend
#https://www.simplilearn.com/tutorials/python-tutorial/python-loops

number = int()
while number<10:
    number = int(input("please enter a number between 0 and 10:"))
    #create new number
    newNumber = number + 1
    print (f"{number} plus one is {newNumber}")
print ("Too high!")

