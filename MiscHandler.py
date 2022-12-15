from CommandHandler import CommandHandler


class HelloHandler(CommandHandler):
    def __init__(self, command, description):
        super().__init__(command, "Print a hello message")

    def handle(self, args):
        # print a hello message
        return "Hello!"