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

def get_search_url(query):
    query = query.strip().replace(":", "%3A").replace("+", "%2B").replace("&", "%26").replace(" ", "+")
    return "http://www.google.com/search?hl=en&q=site:docs.python.org/3/+{}".format(query)

def get_html(url):
    try:
        request = requests.get(url)
        return request.text
    except:
        logging.error("Error accessing:", url)
        return None

def search(query):
    url = get_search_url(query)
    html = get_html(url)
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        try:
            item = soup.find("div", attrs = { "class" : "g" })
            link = item.find("cite").text
            desc = item.find("div", attrs = {"class": "_sPg"}) or item.find("span", attrs = { "class" : "st" })
            desc = desc.text.replace('\n', '').strip()
        except:
            return "Could not find help on _{}_.".format(query), None
    return desc, link

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
                        desc, link = search(query)
                        resp = "{}{}".format(desc, '\n'+link if link is not None else '')
                        client.rtm_send_message(event['channel'], resp)
                    except Exception:
                        log.exception('Error!')
            time.sleep(1)
