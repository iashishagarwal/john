# john
John the ultimate copilot

######Setup
1. First, make sure you have pip3 and virtualenv installed on your system. If you do not have them installed, you can install them by running the following commands:

```
python3 -m pip install pip
python3 -m pip install virtualenv 
```

2. Once you have pip3 and virtualenv installed, create a new virtual environment by running the following command:
```
virtualenv <env_name>


Skip follow steps if the virtualenv command executed successfull. On macOS, if virtualenv is not found. Uninstall virtualenv and rerun as sudo)
> python3 -m pip uninstall virtualenv 
> sudo pip3 install virtualenv
```

Replace <env_name> with the desired name for your virtual environment.

3. Activate the virtual environment by running the following command:
```
source <env_name>/bin/activate
```

4. Use pip3 to install the openai and colorama libraries by running the following commands:
```
pip3 install openai
pip3 install colorama
```

5. Next, you will need to obtain an API key for the OpenAI API. You can do this by signing up for an account at the OpenAI Developer Portal (https://beta.openai.com/signup/developer).

6. Once you have obtained an API key, set it as the value of the OPENAI_API_KEY environment variable in your shell. This will allow you to use the OpenAI API in your Python programs. To set the environment variable, you can use the export command in bash or the set command in PowerShell, like this:
```
# Bash
export OPENAI_API_KEY=<your_api_key>

# PowerShell
set OPENAI_API_KEY=<your_api_key>
```

Replace <your_api_key> with your actual API key.

7. Copy john.py by gitclone repo 

```
cd <env_name>
git clone git@github.com:iashishagarwal/john.git
cd john
python3 john.py
```

8. When you are finished using the virtual environment, you can deactivate it by running the following command:

```
deactivate
```


##### Usage
```
usage: john.py [-h] [-d] [-t TEMPERATURE] [-m MAXTOKENS]

optional arguments:
  -h, --help            show this help message and exit
  -d, --debug           Enable debug mode (default : off)
  -t TEMPERATURE, --temperature TEMPERATURE
                        Provide a float value, Higher values means the model will take more risks. Try 0.9 for more creative applications, and 0 (argmax sampling) for ones with a well-defined answer. Defaults to 0.3.
  -m MAXTOKENS, --maxtokens MAXTOKENS
                        The token count of your prompt plus max_tokens cannot exceed the model's context length. Most models have a context length of 2048 tokens (except for the newest models, which support 4096). Defaults to 150.
```

##### Example

###### Example 1
<pre>
Debug mode is not enabled.
Temperature: 0.3
Maximum number of tokens: 150
Prompt: write an essay outline for civil war


I. Introduction
A. Definition of Civil War
B. Overview of Causes of Civil War

II. Causes of the Civil War
A. Slavery
B. State’s Rights
C. Economic and Social Differences

III. Impact of the Civil War
A. Impact on the Economy
B. Impact on Society

IV. Conclusion
A. Summary of Causes and Impact of the Civil War
B. Reflection on the Legacy of the Civil War
</pre>
###### Example 2
<pre>
Prompt: write an email requesting status of my house project from Mountain view city department

Subject: Request for Status of House Project

Dear Mountain View City Department,

I am writing to request an update on the status of my house project. I submitted the necessary paperwork and plans to your department several weeks ago and I am eager to learn the status of my application.

I understand that the process can take some time, but I am eager to move forward with my project and would appreciate any information you can provide.

Thank you for your time and consideration.

Sincerely,
[Your Name]
</pre>
###### Example 3
<pre>
Prompt: what are the top 5 things I should know about roman mythology


1. The gods and goddesses of Roman mythology were based on the gods and goddesses of Greek mythology.

2. The most important gods in Roman mythology were Jupiter, Juno, and Minerva.

3. Roman mythology was heavily influenced by the Etruscans, who were a people who lived in Italy before the Romans.

4. Roman mythology was used to explain natural phenomena and to provide moral guidance.

5. Roman mythology was also used to explain the origin of Rome and its people.
</pre>
###### Example 4
<pre>
Debug mode is not enabled.
Temperature: 0.3
Maximum number of tokens: 150
Prompt: summarize this text "High levels of debt have also constrained policymakers’ room for manoeuvre. Across the g7 group of rich, powerful countries, private debt has risen by the equivalent of 30 percentage points of gdp since 2000. Even small declines in cash flows could make servicing the debt harder. This means politicians quickly intervene when anything goes wrong. Their focus is keeping the show on the road—avoiding a repeat of the global financial crisis of 2007-09—rather than accepting pain today as the price of a brighter future.

Quite what would push the West in a new direction is unclear. There is no sign of a shift just yet, beyond the misguided attempts of Mr Trump and Ms Truss. Would another financial crisis do the job? Will a change have to wait until the baby-boomers are no longer around? Whatever the answer, until growth speeds up Western policymakers must hope their enemies continue to blunder."


This text is discussing how high levels of debt have limited the ability of policymakers to make decisions. It also mentions that private debt has risen significantly since 2000, and that politicians are focused on avoiding a repeat of the global financial crisis rather than accepting short-term pain for long-term gain.
</pre>
