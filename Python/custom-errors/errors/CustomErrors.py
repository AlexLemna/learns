import traceback
import sys


class CustomError(Exception):
    """Base class for exceptions in the 'custom-errors' project."""
    def __init__(self, ARG_errortype="Custom Error", ARG_message="A (custom!) error has occured! This is a default error message."):
        # self.errortype = ARG_errortype
        self.message = ARG_message
        pass
        
    
    # an abstract method to print an error message header
    def header(self, errortype):
        if type(errortype) is not str:
            errortype = str(errortype)
        else: pass
        num_of_dashes = round ((58 - len (errortype)) /2)
        print ("-"*num_of_dashes, errortype, "-"*num_of_dashes)


class MyFirstError(CustomError):
    """My first custom error!"""
    def __init__(self):
        message = "MyFirstError occured!"
        self.message = message
        CustomError.__init__(self, ARG_errortype="MyFirstError" , ARG_message=message)
        CustomError.header(self, errortype="MyFirstError")
        print (message)
        print ()


class MySecondError(CustomError):
    """My second custom error!"""
    def __init__(self):
        CustomError.__init__(self)
        CustomError.header(self, errortype="MySecondError")