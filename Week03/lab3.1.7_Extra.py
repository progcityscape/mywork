# extra work for week 3
# cannot concatenate string and int

# message = 'I have eaten ' + 99 + ' burritos.'
# print(message)

message = 'I have eaten ' + str(99) + ' burritos.'
print(message)

# outdo the number of burritos

burritos = int(input("How many burritos have you eaten? "))

message = 'I have eaten ' + str((burritos+1)) + ' burritos.'
print(message)
