import random 
print("Please, enter the count of numbers.")
numbersCount = int(input())
print ("Enter the below number of random numbers.")
below = int(input())
print ("Enter the top number of random numbers.")
top = int(input())
i = 0
random_numbers_file = open ("random_numbers_file.txt", "wt")
while i < numbersCount:
 number = random.randint(below, top)
 random_numbers_file.write (str(number)+'\n')
 i = i + 1
random_numbers_file.close()
print ("The file is generated. The file's name is random_numbers_file.")