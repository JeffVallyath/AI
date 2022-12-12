import os

import openai

from CommandHandler import CommandHandler

# Set OpenAI API key
openai.api_key = "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"

# Define function to summarize a document


class SummarizeHandler(CommandHandler):
    def __init__(self, command, description):
        super().__init__(command, "Print a hello message")

    def handle(self, args):
        # print a hello message
        with open(args[0],) as f:
            data = f.readlines()
        sum = self.summarize(data)
        print(sum)

    def summarize(self, document):
        # Use OpenAI language model to generate summary of document
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"Please summarize the following document:\n\n{document}",
            temperature=0.5,
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
        print(ans)

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