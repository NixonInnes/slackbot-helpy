import os
import logging
import requests
from bs4 import BeautifulSoup
from slackclient import SlackClient

logging.basicConfig(filename='helpy.log', level=logging.INFO)
log = logging.getLogger('ex')

token = os.environ.get('SLACK_TOKEN')
client = SlackClient(token)
channel = 'bot-test'

logging.debug(client.api_call('api.test'))

def get_help(mod):
    url = 'https://docs.python.org/3/library/'+mod+'.html#module-'+mod
    req = requests.get(url)
    if not req.ok:
        return "Could not find help on _{}_.".format(mod)
    soup = BeautifulSoup(req.text, 'html.parser')
    para = soup.find_all('p')[2].string.strip('\n')
    if len(para) > 250:
        para = para[:250]
    resp = para + "\n" + req.url
    return resp

if client.rtm_connect():
    while True:
        new_events = client.rtm_read()
        for event in new_events:
            if 'type' in event and 'text' in event and event['type'] == 'message':
                logging.info(event['user']+':'+event['text'])
                msg = event['text']
                if msg.split()[0] == 'helpy':
                    msg = ' '.join(msg.split()[1:])
                    try:
                        resp = get_help(msg)
                        client.rtm_send_message(channel, resp)
                    except Exception:
                        log.exception('Error!')

