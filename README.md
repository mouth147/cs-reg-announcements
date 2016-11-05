# Rutgers CS Announcements
Last semester I missed out on another class opening because the only thing they did was update a webpage that I didn't know existed. 

This script parses the webpage's HTML and lets me know if there's any new announcements.

### Libraries Used
* [requests](https://pypi.org/project/requests/)
* [beautifulsoup4](https://pypi.org/project/requests/)
* [twilio](https://pypi.org/project/twilio/)

# Installation
1. Clone this repository to your folder
2. Create a virtual environment by running `virtualenv venv`
3. Activate this environment `source venv/bin/activate`
4. Install requirements `pip install -r requirements.txt`
5. Copy over `account-example.py` to `account.py` with appropriate credentials if you plan on using Twilio for notifications
6. Depending on how often you want to run it edit your [crontab](http://www.adminschoice.com/crontab-quick-reference) to run as frequently as you want
