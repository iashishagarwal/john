# john
John the ultimate copilot

#####Setup
<pre>
1. Install pip3
2. Install openai using pip3 
3. Get openai api key
4. set api key to OPENAI_API_KEY variable in your shell
</pre>

##### Usage
<pre>
usage: buddy.py [-h] [-d] [-t TEMPERATURE] [-m MAXTOKENS]

optional arguments:
  -h, --help            show this help message and exit
  -d, --debug           Enable debug mode
  -t TEMPERATURE, --temperature TEMPERATURE
                        Temperature value
  -m MAXTOKENS, --maxtokens MAXTOKENS
                        Maximum number of tokens
</pre>
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
Prompt: write a happy holidays post for my engineering organization

Happy Holidays from the Engineering Department! We hope you all have a safe and joyous holiday season. We are thankful for all the hard work and dedication that each of you have put in this year. We look forward to continuing to work together in the new year and making great strides in engineering! Wishing you all a wonderful holiday season!
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
