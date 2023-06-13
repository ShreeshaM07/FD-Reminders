# FD-Reminders
A python program which eases the tedious task of remembering when exactly an FD gets matured so as to renew it or withdraw it from Bank.
The program reads data from a csv file with all the data and calculates the time remaining for a FD to mature.
It then uses google calenedar API to add all these as events into the user's google calendar setting a reminder automatically.
## Installation
- `pip install pandas`
- `pip install csv`
- `pip install requests`
- `pip install datetime`
- `pip install pip install google-api-python-client`
- `pip install google-auth-oauthlib`
## Requirements
Create a google cloud console account and add it as your project and set up OAUTH client ID.
Enable `Google Calendar API`.
Download the `json` file and link it to `cal_setup.py`.
Run the code and allow all the google sign in pop ups.
