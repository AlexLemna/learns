import cmd


class MyCMD (cmd.Cmd):
    intro = "Welcome to my sample command-line-ish prompt. Type help or ? to list commands.\n"
    prompt = "> "

    def do_add (self, user_input):
        numbers = user_input.split()
        if len(numbers) != 2:
            print ("Please restrict yourself to two numbers only, please.")
        
        try:
            numbers = [int(i) for i in numbers]
        except ValueError:
            print ("Please enter numbers, not letters or other symbols.")
        print (numbers[0] + numbers[1])

if __name__ == "__main__":
    MyCMD().cmdloop()