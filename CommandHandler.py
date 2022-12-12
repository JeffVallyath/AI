import datetime
from datetime import date

# define a dictionary of command handler classes
handlers_help = {
    "hello": "HelloHandler",
    "echo": "EchoHandler",
    "add": "AddHandler",
    "summary": "SummarizeHandler",
    "date": "DateHandler",
    "quit": "QuitHandler",
    "time": "TimeHandler",
    "help": "HelpHandler",
}

class CommandHandler:
    def __init__(self, command, description):
        self.command = command
        self.description = description

    def handle(self, args):
        raise NotImplementedError


class DateHandler(CommandHandler):
    def __init__(self, command, description):
        super().__init__(command, "Print Date")

    def handle(self, args):
        # print the arguments back to the user
        today = date.today()
        print("Today's date:", today)

class TimeHandler(CommandHandler):
    def __init__(self, command, description):
        super().__init__(command, "Print Date")

    def handle(self, args):
        # print the arguments back to the user
        now = datetime.datetime.now()

        print("Today's time:%s"% now.time())

class HelpHandler(CommandHandler):
    def __init__(self, command, description):
        super().__init__(command, "Print Date")

    def handle(self, args):
        # print the arguments back to the user
        for key in handlers_help:
            print(key)


class AddHandler(CommandHandler):
    def __init__(self, command, description):
        super().__init__(command, "Add the arguments together")

    def handle(self, args):
        # convert the arguments to integers and add them together
        result = sum(int(arg) for arg in args)
        print(result)


class QuitHandler(CommandHandler):
    def __init__(self, command, description):
        super().__init__(command, "Quit the program")

    def handle(self, args):
        # exit the program
        print("Goodbye!")
        exit()
