# define the base class for command handlers

# define the different command handler classes

# this imports the command handler which as the name suggests handles the commands that aren't a full string but rather the kewords
from CommandHandler import *
#this imports the library that allows for the input that the user inputted to be echoed back in the way that the AI sees it as 
from EchoHandler import EchoHandler
from MiscHandler import *
#we use the OpenAI framework so that it can respond to questions
from OpenAI import *

#these are the keywords that the bot would detect that you can do certain commands with, an wont be considered as an actual request unless not the first word, help is the command to see the list of commands
handlers = {
    "hello": HelloHandler,
    "echo": EchoHandler,
    "add":   AddHandler,
    "summary": SummarizeHandler,
    "date": DateHandler,
    "quit": QuitHandler,
    "time": TimeHandler,
    "help": HelpHandler,
    "$": StockHandler,
}


from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from requests import Session

def set_palette(app):
    app.setStyle("Fusion")
    darkPalette = app.palette()
    darkPalette.setColor(QPalette.ColorRole.Window, QColor(53, 53, 53))
    darkPalette.setColor(QPalette.ColorRole.WindowText, Qt.GlobalColor.white)
    darkPalette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.WindowText, QColor(127, 127, 127), )
    darkPalette.setColor(QPalette.ColorRole.Base, QColor(42, 42, 42))
    darkPalette.setColor(QPalette.ColorRole.AlternateBase, QColor(66, 66, 66))
    darkPalette.setColor(QPalette.ColorRole.ToolTipBase, Qt.GlobalColor.white)
    darkPalette.setColor(QPalette.ColorRole.ToolTipText, Qt.GlobalColor.white)
    darkPalette.setColor(QPalette.ColorRole.Text, Qt.GlobalColor.white)
    darkPalette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Text, QColor(127, 127, 127))
    darkPalette.setColor(QPalette.ColorRole.Dark, QColor(35, 35, 35))
    darkPalette.setColor(QPalette.ColorRole.Shadow, QColor(20, 20, 20))
    darkPalette.setColor(QPalette.ColorRole.Button, QColor(53, 53, 53))
    darkPalette.setColor(QPalette.ColorRole.ButtonText, Qt.GlobalColor.white)
    darkPalette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.ButtonText, QColor(127, 127, 127))
    darkPalette.setColor(QPalette.ColorRole.BrightText, Qt.GlobalColor.red)
    darkPalette.setColor(QPalette.ColorRole.Link, QColor(42, 130, 218))
    darkPalette.setColor(QPalette.ColorRole.Highlight, QColor(42, 130, 218))
    darkPalette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Highlight, QColor(80, 80, 80), )
    darkPalette.setColor(QPalette.ColorRole.HighlightedText, Qt.GlobalColor.white)
    darkPalette.setColor(QPalette.ColorGroup.Disabled, QPalette.ColorRole.HighlightedText, QColor(127, 127, 127), )
    app.setPalette(darkPalette)

# GUI:
app = QApplication([])
text_area = QPlainTextEdit()
#text_area.setFocusPolicy(Qt.NoFocus)
message = QLineEdit()
layout = QVBoxLayout()
layout.addWidget(text_area)
layout.addWidget(message)
window = QWidget()
window.setLayout(layout)

#sets the background color of the gui
set_palette(app)

#shows the final window of the gui
window.show()

# Event handlers:
def send_message():
    new_message = message.text()
    text_area.clear()
    text_area.appendPlainText(new_message+"\n")    
    input_str = new_message

    # split the input string into tokens (separated by whitespace)
    tokens = input_str.strip().split()

    # if there are no tokens, go to the next iteration of the loop
    if not tokens:
        return

    # get the command and any arguments rom the tokens
    command = tokens[0]
    #setting variable args
    args = tokens[1:]

    # check if the command is in the dictionary of handlers
    if command in handlers:
        # create an instance of the corresponding class
        handler = handlers[command](command, "")
        # call the handle() method and pass in the arguments
        response = handler.handle(args)
        text_area.appendPlainText(response) 
    else:
        # if the command is not recognized, print an error message
        args = tokens[:]
        handler = ChatbotHandler(command, "")
        response = handler.handle(args)
        text_area.appendPlainText(response) 


def display_new_message():
    pass

# Signals:
message.returnPressed.connect(send_message)
timer = QTimer()
timer.timeout.connect(display_new_message)


app.exec()

# define the main loop

    