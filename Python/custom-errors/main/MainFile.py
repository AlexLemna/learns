import sys
import traceback

from errors import CustomErrors


def menu():
    print ("ERRORS:")
    print ("   0. CustomErrors (GENERIC CLASS)")
    print ("   1. MyFirstError")
    print ("   2. MySecondError")
    print ("   3. PLACEHOLDER: Custom Error 3")
    print ("  10. TypeError")
    print (" Any. NotImplementedError")
    print()


def choose_error(ARG_error_code):
    if ARG_error_code == "0":
        raise CustomErrors.CustomError
    elif ARG_error_code == "1":
        raise CustomErrors.MyFirstError
    elif ARG_error_code == "2":
        raise CustomErrors.MySecondError
    elif ARG_error_code == "3":
        print ("Placeholder!")
        print ()
    elif ARG_error_code == "10":
        raise TypeError
    else:
        raise NotImplementedError
    

def mainfunc():
    menu()
    user_input = input ("What error should we raise? ")
    try:
        choose_error (user_input)
    except CustomErrors.CustomError as e:
        e.header(e)
        e.message
    except Exception:
        print ("Exception in user code:")
        print ("-"*60)
        traceback.print_exc(file=sys.stdout)
        print ("-"*60)

