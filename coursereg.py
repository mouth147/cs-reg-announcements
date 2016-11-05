import requests, bs4
from twilio.rest import TwilioRestClient
from account import ACCOUNT_SID, AUTH_TOKEN, to_number, from_number

'''
Twilio Send Message
'''
def send_message(message):
    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    text = client.messages.create(to = to_number, from_ = from_number, body = message)

'''
Gets rid of non-ascii characters
'''
def remove_control_characters(str):
     return ''.join([i if ord(i) < 128 else ' ' for i in str])

# SSL Certificate isn't available so we set verify to False
res = requests.get('https://www.cs.rutgers.edu/course/registration', verify = False)

try:
    res.raise_for_status()
except Exception as e:
    print 'Error during request: %s' % (e)

source_file = bs4.BeautifulSoup(res.text, "html.parser")
'''
There's only one unordered list without a
tag and that's the one we need to worry
about so we get the first one from the
document and go through it's children.
'''

ul_tag = source_file.find("ul", class_ = False, id = False)

for li in ul_tag.children:
    new_str = remove_control_characters(li.string)
    '''
    Sometimes we get odd characters that don't belong.
    By checking the string size to be greater than 10,
    we're reassuring that the string we're writing into
    our file has meaning.
    '''
    if len(new_str) >= 10:
        if new_str not in open('announcements.txt').read():
            print("New Announcement: %s") % (new_str)
            send_message(new_str)
            open('announcements.txt', 'a').write(new_str + '\n')

