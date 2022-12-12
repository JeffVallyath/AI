from CommandHandler import CommandHandler


class EchoHandler(CommandHandler):
    def __init__(self, command, description):
        super().__init__(command, "Echo the arguments back to the user")

    def handle(self, args):
        # print the arguments back to the user
        print(" ".join(args))