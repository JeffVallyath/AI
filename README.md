# AI
This is my AI project. In this project, my goal is to have working code in which this program can respond to any input that the user inputs, even if it is random.

I currently am utilizing Open AI's API to actually have the capacity to respond to questions, and I am adding the ability for it to browse the internet as well, something that Open AI cannot. I have just added a GUI and a stock ticker function for my AI project for some extra features in addition to all the previous features it currently possessed.

A future goal may be to add a way to summarize more efficiently and accurately using the summarize command.


Commands:
Use the help command to see all the possible commands of what we added                                    How to call these commands

hello command - Has the bot give a greeting.                                                              Written as hello
echo command - can repeat whatever user inputs                                                            Written as echo <what you want it to repeat>
summary command - WIP, but it can summarize a .txt file as long as you provide the file path              Written as summary <filepath/filename has to be a .txt file> 
date command - will tell the date of today                                                                Written as date
time command - will tell the time of today                                                                Written as time
help command - as previously explained, can see every command possible                                    Written as help
$ command - will show current stock prices                                                                Written as $ <stock symbol for example, AAPL)


The MarkovChain is a more complex command, so it works in two parts:
1. Use MarkovTrain <file name/file path>
2. Use MarkovGen <number of words you want to generate in the markov chain>






API key:
The API key will not work because of security issues, it automatically disables the key so I will send in outlook the api key, copy the api key and then go here https://github.com/JeffVallyath/AI/blob/main/OpenAI.py#L8 and change the api key to the key in outlook. 




Dependencies:
pip install OpenAI
pip install pyQt6
pip install yfinance
