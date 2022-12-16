import os

import openai

from CommandHandler import CommandHandler

#I am currently utilizing the open api key which allows me to have the capacity to be able to respond to questions, which takes out a major hurdle in the way, due to the api key, however there are some features that the chatbot can't do that I use this api key fpr
openai.api_key = "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"



#this is a subclass
class SummarizeHandler(CommandHandler):
    def __init__(self, command, description):
        super().__init__(command, "Print a hello message")

    def handle(self, args):
        # print a hello message
        with open(args[0],) as f:
            data = f.readlines()
        sum = self.summarize(data)
        return sum

    def summarize(self, document):
        # Use OpenAI language model to generate summary of document
        response = openai.Completion.create(
            #the engine that OpenAI uses to process the input
            engine="text-davinci-002",
            prompt=f"Please summarize the following document:\n\n{document}",
            #allows the result to be more varied/creative the more temperature the more original
            temperature=0.5,
            #the more you increase this the more complex the answers would be but the tradeoff is that it 
            #takes more time to process the answer
            max_tokens=100,
            top_p=1.0,
            frequency_penalty=0,
            presence_penalty=0
        )

        # Extract summary from response
        summary = response["choices"][0]["text"]

       # Use natural language processing to further refine summary
       #summary = extract_important_sentences(summary)
        #summary = extract_keywords(summary)

        # Return refined summary
        return summary


class ChatbotHandler(CommandHandler):
    def __init__(self, command, description):
        super().__init__(command, "Print a hello message")

    def handle(self, args):
        # print a hello message
        print(args)
        question = " ".join(args)
        print("question:%s" % question)
        ans = self.answer(question)
        return(ans)

    def answer(self, question):
        # Use OpenAI language model to generate summary of document

        prompt = f'Human: {question}\nAI:'
        print("prompt:", prompt)
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            temperature=0.5,
            max_tokens=100,
            top_p=1.0,
            frequency_penalty=0,
            presence_penalty=0
        )

        # Extract summary from response
        ans = response["choices"][0]["text"]

       # Use natural language processing to further refine summary
       #summary = extract_important_sentences(summary)
        #summary = extract_keywords(summary)

        # Return refined summary
        return ans