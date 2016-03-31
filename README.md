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
- [beautifulsoup4](https://pypi.python.org/pypi/beautifulsoup4)

###Installation
Clone this repository, or download the archive. You will need to set an environment variable 'SLACK_TOKEN', for the bot to use (available in your slack channel configuration).  
Create a new folder, called *logs*, in the same directory as *app.py*, and now all you need to do is run `python app.py`.
