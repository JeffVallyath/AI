from CommandHandler import CommandHandler

#this may not be as necessary, but basically this is a subclass which would just tell the user what it saw out of its message, its nice for debugging but it may not be needed in the final prototype
class EchoHandler(CommandHandler):
    def __init__(self, command, description):
        super().__init__(command, "Echo the arguments back to the user")

    def handle(self, args):
        # print the arguments that it registered as a string back to the user
        print(" ".join(args))