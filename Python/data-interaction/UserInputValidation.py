# IMPORTING GLOBAL MODULES
import sys
    # So we can gracefully exit the program when the user commands.
import textwrap
    # We've got some big paragraphs of text that might be printed to the terminal, and I want to mkae sure the words aren't broken up across lines.

# DEFINING FUNCTIONS
def DisplayMenu(): # Displays the main menu
    print (30 * "-")
    print ("     1. Lorem ipsum.")
    print ("     2. Integer check.")
    print ("X or 0. Exit program.")
    print()

def LoremIpsum(): # Displays a paragraph of "lorem ipsum" text, using the "textwrap.fill" function to keep it viewable on narrow console screens and avoid starting new lines in the middle of a word.
    print ( "LOREM IPSUM" )
    print ( textwrap.fill ("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras euismod malesuada ante, sit amet blandit nibh consequat eu. Aenean ligula est, malesuada et velit vel, pharetra convallis mauris. Curabitur non consequat tellus, ut condimentum sem. Cras suscipit accumsan orci, vel rutrum ante hendrerit sit amet. Duis suscipit arcu ac tortor tristique, sit amet varius leo fringilla. In ex nulla, egestas a rhoncus nec, aliquet ac diam. Proin id faucibus risus. In tempus congue mattis. Cras nec vehicula nisl. Curabitur ultrices risus faucibus maximus venenatis. Morbi consectetur eros non tristique imperdiet.", width = 70))

def IntegerCheck(): # Determines if user input is an integer.
    userInput = input ("Not sure if something is an integer? Enter it and find out: ")
    try: 
        userInteger = int (userInput)
        print ("Yes, ", userInteger, " is an integer.")
    except:
        print ("Nope, that's not an integer.")

# COMMAND LINE INTERFACE SECTION
print()
print ("This is a program to test my programming skills around validating user-supplied inputs. Let's begin... what would you like to do?")

loopMain = True
while loopMain is True:
    DisplayMenu()
    menuChoice = input ( "Enter the number for one of the options above: ")
    print()

    if menuChoice == '1':
        print()
        LoremIpsum()
        print()
        input ("Press any button to see to the main menu.")
    if menuChoice == '2':
        print()
        IntegerCheck()
        print()
        input ("Press any button to see to the main menu.")
    elif menuChoice == '0' or menuChoice == 'X' or menuChoice == "x":
        sys.exit(0)
    else:
        print ("Look, I'm just a computer program. I've got all the time to waste in the world, and I don't get bored. You can keep entering invalid inputs, or you can actually follow instructions. Your call.")
