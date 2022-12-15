import datetime
from datetime import date
import yfinance as yf

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

#this is the super class which initializes all the commands correlated with the corresponding subclasses
class CommandHandler:
    def __init__(self, command, description):
        self.command = command
        self.description = description

    def handle(self, args):
        raise NotImplementedError

#this is a subclass of the command handler class which handles the date command and when the date command is registered it will print the current date
class DateHandler(CommandHandler):
    def __init__(self, command, description):
        super().__init__(command, "Print Date")

    def handle(self, args):
        # print the arguments back to the user
        today = date.today()
        return "Today's date:%s"%today

#this a subclass of the command handler class which handles the time command and when the time command is registered it will print the current time
class TimeHandler(CommandHandler):
    def __init__(self, command, description):
        super().__init__(command, "Print Date")

    def handle(self, args):
        # print the arguments back to the user
        now = datetime.datetime.now()

        return "Today's time: %s"% now

#this is a subclass of the command handler class which handles the help command and when the help command is registered it will print all the possible commands one can use in this chatbot
class HelpHandler(CommandHandler):
    def __init__(self, command, description):
        super().__init__(command, "Print Date")

    def handle(self, args):
        # print the arguments back to the user
        for key in handlers_help:
            print(key)

#this is a subclass of the add handler which handles the add command which can summarize two numbers, the thing is this subclass may not be necessary considering the AI already has a inbuilt calculator
class AddHandler(CommandHandler):
    def __init__(self, command, description):
        super().__init__(command, "Add the arguments together")

    def handle(self, args):
        # convert the arguments to integers and add them together
        result = sum(int(arg) for arg in args)
        print(result)

#this is a subclass of the command handler which handles the quit command and when the quit command s registered will print Goodbye and quit the program 
class QuitHandler(CommandHandler):
    def __init__(self, command, description):
        super().__init__(command, "Quit the program")

    def handle(self, args):
        # exit the program
        print("Goodbye!")
        exit()

class StockHandler(CommandHandler):
    def __init__(self, command, description):
        super().__init__(command, "Add the arguments together")

    def handle(self, args):
        # convert the arguments to integers and add them together
        stock = args[0]

        # Get the stock info
        stock_info = yf.Ticker(stock)

        # Get the stock quotes
        stock_quotes = stock_info.info

        # Print the stock quotes
        #print(stock_quotes)

        return f"Current price: {stock_quotes['regularMarketPrice']}"