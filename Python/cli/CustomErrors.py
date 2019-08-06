import sys

# define Python user-defined exceptions
class CustomError(Exception):
    """Base class for other exceptions"""
    pass

class BadInput(CustomError):
    """Raised when user input is not recognized."""

    def __init__(self):
        pass
    
    def errormessage(self, x):
        print ("BAD INPUT ERROR: ", end="")
        try:
            x
            print (f"'{x}' is not a recognized command.")
        except NameError:
            print ("Variable 'user_input' is not defined.")
        except:
            print (f"An unexpected error ({sys.exc_info()[0]}) occured.")
            raise
