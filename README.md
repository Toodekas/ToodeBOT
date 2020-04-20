# ToodeBOT
This is a BOT that communicates with an artaficial intelligence called Inspirobot and sends a specified group a motivational quote image, every day.

To use this, please install the fb chat API
```pip install fbchat```
For more information about the installation
https://fbchat.readthedocs.io/en/stable/install.html

In the code you must change the "user" and "pass" section and put in your facebook username and password
You also need to change the variable thread_id, to find out the id of your group, open messenger.com and select the group that you want to have automatic quotes generated to. Then in the URL the last numbers is the thread_id just copy and replace that in the code and run. 

On windows I reccomend opening the folder through cmd and running it from cmd (or any other editor, cmd is good if you want to have it run in the background and send a motivational quote to your group every day) 'python inspirashun.py'

On Linux just run the python file in the terminal 'python3 inspirashun.py'


