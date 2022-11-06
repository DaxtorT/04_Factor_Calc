# Functions go here

# Number checker function, should be between (and including) 1 and 200
def num_check(question):
    valid = False
    while not valid:

        error = "Please enter an integer that is more than zero"

        try:

            # Ask user to enter a number
            response = int(input(question))

            # Checks number is more than zero
            if 1 <= response <= 200:
                return response

            # Outputs error if input is invalid
            else:
                print(error)
                print()
            
        except ValueError:
            print(error)

# Factor checking and listing function
def to_factor():

# Create list for factors
    my_list = []

# Get number to factorise
    var_integer = num_check("Enter a number to be factorised: ")

# Find the factors (hint: use modulo)
# If the number to factorise is 1, tell the user it's unity
    to_stop = var_integer**0.5
    to_stop = int(to_stop)
    for item in range (1, to_stop + 1):

        remainder = var_integer % item

    # Output the factors as a sorted list
        if remainder == 0:
            factor = var_integer // item

            my_list.append(item)

            if factor not in my_list:
                my_list.append(factor)

    my_list.sort()

    if len(my_list) == 1:
        print(my_list)
        print("We have a Unity")

    elif len(my_list) == 2:
        print(my_list)
        print("We have a Prime Number")

    elif len(my_list)%2 == 1:
        print(my_list)
        print("We have a Perfect Square")

    else:
        print(my_list)


# Main routine goes here
keep_going = ""
while keep_going == "":
    
    factorise = to_factor()
    print()

    keep_going = input("Press <enter> to go again or any key to quit")

print()
print("We Are Done")