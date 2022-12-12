# define the base class for command handlers

# define the different command handler classes

from CommandHandler import *
from EchoHandler import EchoHandler
from MiscHandler import *
from OpenAI import *

handlers = {
    "hello": HelloHandler,
    "echo": EchoHandler,
    "add":   AddHandler,
    "summary": SummarizeHandler,
    "date": DateHandler,
    "quit": QuitHandler,
    "time": TimeHandler,
    "help": HelpHandler,
}


# define the main loop
while True:
    # print a prompt and get the user input
    input_str = input("> ")

    # split the input string into tokens (separated by whitespace)
    tokens = input_str.strip().split()

    # if there are no tokens, go to the next iteration of the loop
    if not tokens:
        continue

    # get the command and any arguments from the tokens
    command = tokens[0]
    args = tokens[1:]

    # check if the command is in the dictionary of handlers
    if command in handlers:
        # create an instance of the corresponding class
        handler = handlers[command](command, "")
        # call the handle() method and pass in the arguments
        handler.handle(args)
    else:
        # if the command is not recognized, print an error message
        handler = ChatbotHandler(command, "")
        handler.handle(args)
