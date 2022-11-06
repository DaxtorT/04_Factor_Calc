# Checks if the number is more than 0
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


# Main Routine goes here
keep_going = ""
while keep_going == "":
    
    var_integer = num_check("Enter an integer: ")