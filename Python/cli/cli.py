import commands
import CustomErrors

cli_runs = True
cli_prompt = ">"

def cli_main_menu():
    user_input = input (f"r{cli_prompt} ")
    user_input = user_input.rstrip()  # Strips trailing spaces from input
    if user_input == "exit":
        cli_runs = False
        SystemExit()
    elif user_input == "":  # Has the user entered nothing?
        pass
    else:
        try:
            if user_input == "about-program":
                pass
            elif " " in user_input:  # Parsing multiple words
                user_words = user_input.split()
                if user_words[0] in commands.top_level:  # tip: '0' is the first list item
                    print ("I should do something.")
                else:
                    raise CustomErrors.BadInput
            else:
                raise CustomErrors.BadInput
        except CustomErrors.BadInput as e:
            e.errormessage(user_input)


# Main program starts here

cli_runs = True
cli_prompt = ">"
while (cli_runs is True):
    cli_main_menu()
else:
    SystemExit()
