# slackbot-helpy
Helpy is a bot user for [slack](https://slack.com/).  
It will take queries from users and search the Python 3 documentation for an appropriate link. It will return a short paragraph and link to the documentation.  

## Use
Invite helpy into your slack channel, or private message it.  
If you prefix a message with the word *helpy*, the bot will query the documentation using the remaining text.  

e.g.  
**nixoninnes**: helpy io  
**helpy**: The io module provides Python's main facilities for dealing with various types of I/O. There are three main types of I/O: text I/O, binary I/O and ...  
https://docs.python.org/3/library/io.html

## Installation
### Requirements
- [slackbot](https://pypi.python.org/pypi/slackbot)
- [requests](https://pypi.python.org/pypi/requests)

###Installation
Install the above required packages using pip. i.e. `pip install slackbot`  
Clone this repository, or download & extract the archive. You will need to create an environment variable 'SLACK_TOKEN' containing your token for the bot; available from your slack team configuration options.  
Now all you need to do is run `python app.py`!
