# Functions go here

# Puts series of symbols at start and end of text
def statement_generator(text, decoration):

    # Make string with five characters
    ends = decoration * 5

    # Add decoration to start and end of statement
    statement = "{}  {}  {}".format(ends, text, ends)

    print()
    print(statement)

    return ""


# Displays instructions / information
def instructions():

    statement_generator("Instructions / Information", "=")
    print()
    print("Please enter a number that is more than (or equal to) one and less than (or equal to) 200.")
    print()
    print("Complete as many calculations as necessary, pressing <enter> at the end of each calculation or any key to quit.")
    print()
    return ""


# Checks input is a number more than zero
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


# Gets factors, returns a sorted list
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


# Main Routine goes here
# Heading
print (statement_generator("Factors Calculator", "-"))

# Display instructions if user has not used the program before
first_time = input("Press <enter> to see the instructions or any key to continue ")

if first_time == "":
    instructions()

else:
    print()

# Loop to allow multiple calculations per session
keep_going = ""
while keep_going == "":

    comment = ""

    # Starts factorising process...
    factorise = to_factor()


    print()
    keep_going = input("Press <enter> to continue or any key to quit ")
    print()

print()
print("Thank you for using the factor calculator. :)")
print()