# This project uses the OpenAI API (https://beta.openai.com/)

import os
import openai
import argparse
from colorama import Fore, Style

# Create an argument parser
parser = argparse.ArgumentParser()

# Add an argument to the parser
parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode. Default to false.")
parser.add_argument("-t", "--temperature", type=float, default=0.3, help="Defaults to 0.3. Provide a float value, Higher values means the model will take more risks. Try 0.9 for more creative applications, and 0 (argmax sampling) for ones with a well-defined answer.") 
parser.add_argument("-m", "--maxtokens", type=int, default=150, help="Defaults to 150, The token count of your prompt plus max_tokens cannot exceed the model's context length. Most models have a context length of 2048 tokens (except for the newest models, which support 4096).")

# Parse the arguments
args = parser.parse_args()

#Reset all styles
print(Style.RESET_ALL)
print(Style.DIM)

# Check if debug mode is enabled
if args.debug:
  print(Fore.CYAN +"Debug mode is enabled.")
else:
  print(Fore.WHITE +"Debug mode is not enabled.")

# Print the temperature value
print(Fore.WHITE +"Temperature:", args.temperature)

# Print the maximum number of tokens
print(Fore.WHITE +"Maximum number of tokens:", args.maxtokens)

#reset style after printing all tokens
print(Style.RESET_ALL)

#open api key
openai.api_key = os.getenv("OPENAI_API_KEY")

#Start the loop to continously input and output
while True:
  # Take input from the user
  s = input(Fore.MAGENTA + "> ")

  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=s,
    temperature=args.temperature,
    max_tokens=args.maxtokens,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
  )

  # Parse the response
  response_text = response.choices[0].text.strip()

  if args.debug:
    print(Fore.CYAN)
    print(Style.DIM)
    print(response)
    print(Style.RESET_ALL)

  # Print the generated text
  print(Fore.YELLOW + response_text)
  
