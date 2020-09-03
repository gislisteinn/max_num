
#Algorythm:

#problem 1: we need an input from the user, use the input fundction for that
#Problem 2: we are supposed to keep asking him for an input while the input is >= 0 so for that we can use a while loop but we need to start outside the loop
#Problem 3: we need to see if the number he just put in is larger then the last one, if it is that our new number, if not the number remains the old one, lets use a variable





num_int = int(input("Input a number: "))    # Do not change this line
max_int = num_int
while num_int >= 0:
    num_int = int(input("Input a number: ")) 
    if max_int < num_int:
        max_int = num_int

print("The maximum is", max_int)    # Do not change this line