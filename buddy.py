import os
import openai
import argparse

# Create an argument parser
parser = argparse.ArgumentParser()

# Add an argument to the parser
parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode")
parser.add_argument("-t", "--temperature", type=float, default=0.3, help="Temperature value")
parser.add_argument("-m", "--maxtokens", type=int, default=150, help="Maximum number of tokens")

# Parse the arguments
args = parser.parse_args()

# Check if debug mode is enabled
if args.debug:
  print("Debug mode is enabled.")
else:
  print("Debug mode is not enabled.")

# Print the temperature value
print("Temperature:", args.temperature)

# Print the maximum number of tokens
print("Maximum number of tokens:", args.maxtokens)

#open api key
openai.api_key = os.getenv("OPENAI_API_KEY")

while True:
  # Take input from the user
  s = input("Prompt: ")

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
  response_text = response.choices[0].text

  if args.debug:
    print(response)

  # Print the generated text
  print(response_text)


