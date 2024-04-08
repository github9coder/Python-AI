def python_ai():
    """An ai that talks about, and only about Python."""
    # Import all needed packages

    import os
    from openai import OpenAI
    from colorama import Fore, Back, Style
    
    # Set the OpenAI API key

    client = \
        OpenAI(api_key= {your_API_key}
               )
    OpenAI.api_key = os.getenv('OPENAI_API_KEY')

    # define colours to show when interacting with user.

    class color:

        PURPLE = '\033[95m'
        CYAN = '\033[96m'
        DARKCYAN = '\033[36m'
        BLUE = '\033[94m'
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        RED = '\033[91m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
        END = '\033[0m'
        

    # define which words will stop the program.
    word_stop = [
            'quit',
            'exit',
            'bye',
            'end',
            'goodbye',
            'see you'
            ]



    # Define a function to interact with the chat-based language model

    def chat_gpt(user_input):

        # Define the conversation with a system message and user message

        conversation =  [
                    {'role': 'system',
                    'content': "You are a helpful assistant that knows about Python programming. \
                    If the question is not about Python programming or simple maths, you do not have information. \
                    You don't know about: History, science, and anything not about python or maths."}, 
                    {'role': 'user', 'content': user_input}
                    ]

        # Create a chat completion with the given conversation

        completion = \
            client.chat.completions.create(model='gpt-3.5-turbo',
                messages=conversation)

        # Extract and return the AI's response

        return completion.choices[0].message.content

    if __name__ == '__main__':
        print (color.BOLD + color.BLUE + 'PYTHON AI:' + color.END \
              + ' Welcome to Python AI! Type ' + color.RED + color.BOLD \
              + "'exit', 'quit', 'bye', 'goodbye'," + color.END + ' or' \
              + color.RED + color.BOLD + " 'see you' " + color.END \
              +'to end the conversation.')
        
    while True:

        user_input = input('\nYOUR RESPONSE: ')

            # Wait for input.

        if user_input.lower() in word_stop:
            print (color.BOLD + color.BLUE + '\nPYTHON AI:' \
                   + color.END + ' Thank you for using Python AI!')
            break
                
        else:

            #if the user says a word in the list word_stop, print "Thank you for using Python AI", and finish the process.

            response = chat_gpt(user_input)
            print (color.BOLD + color.BLUE + '\nPYTHON AI:'
                   + color.END, response)

python_ai()
