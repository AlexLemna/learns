import time
import struct

try:
    pipe_file = open (r"\\.\pipe\testing", mode="r+b", buffering=0)
    while True:
        length_of_message_string = struct.unpack ("I", pipe_file.read(4))[0]  # Read string length up to 4 bytes
        message_string = f.read(length_of_message_string).decode("ascii")  # Read the string
        pipe_file.seek(0)  # Change stream position to the start of the stream
        print (f"Read: {message_string}")
        time.sleep(1.2)  # Wait 1.2 seconds (simulates "doing something" with the string data?)
        message_string = "Completed: " + message_string
        pipe_file.write (struct.pack ("I", len(message_string)) + message_string.encode("ascii"))  # Write string length and string
        pipe_file.seek(0)
        print (f"Wrote: {message_string}")
except FileNotFoundError:
    raise
