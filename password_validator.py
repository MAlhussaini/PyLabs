""" 
Password validator is a program that validates passwords to match specific rules. For example, the minimum length of the password must be eight characters long and it should have at least one uppercase letter in it. 

A valid password is the one that conforms to the following rules:
 - #// TODO: Minimum length is 5;
 - #// TODO: Maximum length is 10;
 - #// TODO: Should contain at least one number;
 - #// TODO: Should contain at least one special character (such as &, +, @, $, #, %, etc.);
 - #// TODO: Should not contain spaces or invalid charecters.
 - # TODO: Should contain at least one upper Alphabit
 - # TODO: Should contain at least one lower Alphabit 
"""
import logging

# ? Change logging mood to CRITICAL to disable all levels of logging
logging.disable(logging.INFO)
# ? To make the logging outputs in the terminal
logging.basicConfig(level=logging.DEBUG,
                    format=' %(asctime)s - %(levelname)s - %(message)s')


# Debugging sentence with modes (info/Debug). Will be seen throughout the program.
logging.info('Start of the program')

def key():
    '''
    Take a password input and return password string.
    '''
    logging.info('Start of the key function\n')

    password = input("Create a password: ")
    return str(password)

# Key validation for the while loop.
validation = "Waiting input"
# List of all the possible numbers in one character.
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
# List of all the possible special charecters.
spec_chars = "!#$%&()*+,-.:;<=>?@[]^_`{|}~"
# List of all the invalid possible special charecters.
invalid_chars = " \"'\\/"

AZ = []
az = []
for i in range(ord('a'), ord('z')+1):
    az.append(chr(i))
    AZ.append(chr(i).upper())

# Will loop and keep asking for password till it satisfies the condition
while validation != "valid":
    logging.info('Start of the while loop\n')

    # Get the password from the user.
    password = key()
    logging.debug("Returned value is: %s\n" % (password))
    # Flags to check in a password.
    num_detector = 0
    spec_char = 0
    invalid_char = 0
    upper_char = 0
    lower_char = 0

    # Check the length of the password.
    if len(password) < 5 or len(password) > 10:
        print("The minimum length of the password must be between 5 and 10 characters long")
        continue
    logging.info('Password length = %s is valid.\n'%(len(password)))

    # Checks for invalid charecters.
    for char in password:
        logging.debug("charecter value is: %s\n" % (char))
        if char in invalid_chars:
            # Set the flag to 1 if invalid charecter found.
            invalid_char = 1
            break
    # If the flag is 1 the loop repeats.
    if invalid_char == 1:
        print("The password should not contain these charecters.\n \"'\\/ or a space")
        continue
    logging.info('Password invalid_char is valid.\n')

    # Check for a numper in a password.
    for char in password:
        logging.debug("char value is: %s\n" % (char))
        if char in numbers:
            num_detector = 1
            break
    # If the flag is 0 the loop repeats.
    if num_detector == 0:
        print("The password should contain a number.")
        continue
    logging.info('Password num_detector is valid.\n')

    #Checks for special charecters.
    for char in password:
        logging.debug("char value is: %s\n" % (char))
        if char in spec_chars:
            spec_char = 1
            break

    # If the flag is 0 the loop repeats.
    if spec_char == 0:
        print("The password should contain one of these charecters:\n !#$%&()*+,-.:;<=>?@[]^_`{|}~")
        continue
    logging.info('Password spec_char is valid.\n')

    #Checks for lower and upper charecters.
    for char in password:
        logging.debug("char value is: %s\n" % (char))
        if char in az:
            lower_char = 1
        if char in AZ:
            upper_char = 1
        if upper_char+lower_char == 2:
            break

    # If the flag is 0 the loop repeats.
    if lower_char == 0:
        print("The password should contain at least one lower letter.")
        continue
    if upper_char == 0:
        print("The password should contain at least one upper letter.")
        continue
    logging.info('Password spec_char is valid.\n')

    validation = "valid"

# User validation output.
print("You're password %s is strong and %s."%(password,validation))


