import ctypes
import sys

# ada_module = ctypes.CDLL ("libada_module.dylib")  # Creates a "handle" for entire Ada library
ada_module = ctypes.CDLL ("lib/libada_module.dll")  # Creates a "handle" for entire Ada library

# Two "magic" functions needed to properly initialize and finalize the Ada module. Note that these functions return nothing, and Python needs to be explicitly told that via the ".restype" statements so that it knows not to use the nonexistant return values.
ada_module.ada_moduleinit.restype = None
ada_module.ada_moduleinit ()
ada_module.ada_modulefinal.restype = None
ada_module.ada_modulefinal ()

# Similar to the "magic" functions above, we need to tell Python that the say_hello procedure returns nothing.
ada_module.say_hello.restype = None
# Now, we can finally call it.
ada_module.say_hello ()
