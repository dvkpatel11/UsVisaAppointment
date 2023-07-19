# usvisa-appointment

# Env setup

## Pre-requisite
- make sure python3 is installed 

## setup
- create virtaul env: `python -m venv venv`
- activate it: `source venv/bin/activate`
- install requirements: `pip install -r requirements.txt`
- install playwright : `playwright install`
- install playwright browsers : `playwright install-deps`

## config
- create `creds.py` inside code folder and fill values as below

```
user = "abc@gmail.com"
password = "Password"
# get this id from reschedeule page url mentioned below
appointment_id = "12345678"
appointment_url = "https://ais.usvisa-info.com/en-ca/niv/schedule/{}/appointment"
visa_locations = ["Toronto", "Ottawa", "Vancouver", "Calgary"]
check = 12
time_gap = 300
reschedule = False
send_telegram_notification =False
TOKEN = "telegram bot token id"
chat_id = "telegram chat id"
browsers = 10
is_multiple_users = False
applicants_url = "?utf8=✓&commit=Continue"
```

## run(wip)
`python ./code/visa.py`