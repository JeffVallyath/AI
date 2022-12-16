import datetime
from datetime import date
import yfinance as yf
import random
import os
#these two variables are for the markov generator
chain = {}

# define a dictionary of command handler classes
handlers_help = {
    "hello": "Print Hello",
    "echo": "Echo the input",
    "summary": "Summarize a Text file",
    "date": "Print Date",
    "quit": "Quit",
    "time": "Print Time",
    "help": "Show Help",
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
        super().__init__(command, "Help")

    def handle(self, args):
        # print the arguments back to the user
        help = ""
        for key in handlers_help:
            help += key + "    " + handlers_help[key] + "\n"
        return help    



#this is a subclass of the command handler which handles the quit command and when the quit command s registered will print Goodbye and quit the program 
class QuitHandler(CommandHandler):
    def __init__(self, command, description):
        super().__init__(command, "Quit the program")

    def handle(self, args):
        # exit the program
        print("Goodbye!")
        exit()

#this is a subclass of the command handler which handles the Stock
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

class MarkovTrainHandler(CommandHandler):
    def __init__(self, command, description):
        super().__init__(command, "Add the arguments together")

    def handle(self, args):
        data = open(args[0]) 
        index = 1
        #reads every line that it gets from the text in the parameters which can be anything based on what the arg takes in
        data = data.readline()

        #splits the data into a list of words
        data = data.split(' ')
        #creates a for loop that creates a dictionary with a word as a key and a list of possible next words as a value
        for word in data[index:]:
            #this allows us to continue going through every word in the data
            key = data[index-1]
            if key in chain:
                #if the word already appears in chain it appends it to the chain list which at first appears empty but gradually there is more because of the for loop
                chain[key].append(word)
            else:
                #if the key isnt present, it creates a new word
                chain[key] = [word]
            index += 1
        

class MarkovGenHandler(CommandHandler):
    def __init__(self, command, description):
        super().__init__(command, "Add the arguments together")

    def handle(self, args):
        #uses the random library to randomy choose words
        if len(args) < 1:
            return "Missing parameter"
        count = int(args[0])
        word1 = random.choice(list(chain.keys()))
        #captalizes word one to follow propper grammar rules
        message = word1.capitalize()

        while len(message.split(' ')) < count:
            word2 = random.choice(chain[word1])
            word1 = word2
            #adds word 2 to the message
            message += ' ' + word2 
        return message
