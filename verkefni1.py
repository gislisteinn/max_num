
#Algorythm:

#problem 1: we need an input from the user, use the input fundction for that
#Problem 2: we are supposed to keep asking him for an input so for that we can use a while loop
#Problem 3: it should stop if he inputs a negative number so we can put in a bool value that is T if the input is >= 0
#Problem 4: we need to see if the current number is larger than the former number so we need a variable  to keep track of the biggest number
#Problem 4,5: We need to start by asking him for a number before we go into the while loop to set that to the biggest number at the start
#Problem 5: if the current number is larger than the former largest one we need to make it the new biggest one
#Problem 6: When the user ends the program by typing a negative number we want to print the current largest numebr




num_int = int(input("Input a number: "))    # Do not change this line
max_int = num_int
while num_int >= 0:
    num_int = int(input("Input a number: "))
    if num_int > max_int:




print("The maximum is", max_int)    # Do not change this line