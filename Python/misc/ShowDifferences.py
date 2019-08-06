import difflib
import os
import pathlib


def printthings (_arg1, _arg2):
    print (f"Thing1: {_arg1}")
    print (f"Thing2: {_arg2}")


def test (_arg1, _arg2):
    print ("Are they the same? ", end="")
    result = bool (_arg1 is _arg2)
    print (result)


def testascii (_arg1, _arg2):
    print ("Are they the same in ASCII? ", end="")
    _arg1 = ascii (_arg1)
    _arg2 = ascii (_arg2)
    result = bool (_arg1 is _arg2)
    print (result)


def show_diff (_arg1, _arg2):
    result = bool (_arg1 is _arg2)
    if result is False:
        print ("Here's what's different:")
        diff = difflib.ndiff (
            thing1.splitlines(keepends=True),
            thing2.splitlines(keepends=True) )
        print ("".join(diff))
    elif result is True:
        print ("No differences to show.")
    else:
        raise NotImplementedError


def show_diffascii (_arg1, _arg2):
    _arg1 = ascii (_arg1)
    _arg2 = ascii (_arg2)
    result = bool (_arg1 is _arg2)
    if result is False:
        print ("Here's what's different in ASCII:")
        diff = difflib.ndiff (
            thing1.splitlines(keepends=True),
            thing2.splitlines(keepends=True) )
        print ("".join(diff))
    elif result is True:
        print ("No ASCII differences to show.")
    else:
        raise NotImplementedError

# ########## BEGIN ##########
thing1 = "dev-tests"
thing2 = "dev-tests"
printthings (thing1, thing2)
test (thing1, thing2)
testascii (thing1, thing2)
show_diff (thing1, thing2)
show_diffascii (thing1, thing2)
print()

print ("MODULE 'os'")
thing1 = os.path.basename (os.getcwd())
thing2 = "dev-tests"
printthings (thing1, thing2)
test (thing1, thing2)
testascii (thing1, thing2)
show_diff (thing1, thing2)
print()

print ("MODULE 'pathlib'")
thing1 = pathlib.PurePath (pathlib.Path.cwd()).name
thing2 = "dev-tests"
printthings (thing1, thing2)
test (thing1, thing2)
testascii (thing1, thing2)
show_diff (thing1, thing2)
print()


input()
