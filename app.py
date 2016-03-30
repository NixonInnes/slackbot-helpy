import os
import time
import logging
import requests
from bs4 import BeautifulSoup
from slackclient import SlackClient

logging.basicConfig(filename='helpy.log', level=logging.INFO)
log = logging.getLogger('ex')

token = os.environ.get('SLACK_TOKEN')
client = SlackClient(token)

logging.debug(client.api_call('api.test'))

def get_help(query):
    urls = [
        "https://docs.python.org/3/library/"+query+".html",
        "https://docs.python.org/3/reference/"+query+".html"
        ]
    for url in urls:
        req = requests.get(url)
        if req.ok:
            break
    if not req.ok:
        return "Could not find help on _{}_.".format(query)
    soup = BeautifulSoup(req.text, 'html.parser')
    try:
        # This is awful...
        para = soup.find_all('p')[2].string.strip('\n')
    except:
        para = "I couldn't grab any help text, but here's a link..."
    if len(para) > 250:
        para = para[:250] + '...'
    resp = para + "\n" + req.url
    return resp

if client.rtm_connect():
    while True:
        new_events = client.rtm_read()
        for event in new_events:
            if 'type' in event and 'text' in event and 'channel' in event and event['type'] == 'message':
                logging.info('channel: '+event['channel']+', user:'+event['user']+', msg:'+event['text'])
                msg = event['text']
                if msg.split()[0] == 'helpy':
                    query = ' '.join(msg.split()[1:])
                    try:
                        resp = get_help(query)
                        client.rtm_send_message(event['channel'], resp)
                    except Exception:
                        log.exception('Error!')
            time.sleep(1)
