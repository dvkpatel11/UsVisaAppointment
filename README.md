# usvisa-appointment

# Env setup

## Pre-requisite
- make sure python3 is installed 

## setup
- create virtaul env: `python -m venv venv`
- activate it: `source venv/bin/activate`
- install requirements: `pip install -r requirements.txt`
- install playwright : `playwright install`

## config
- create `creds.py` inside code folder and fill values as below

```
user = "abc@gmail.com"
password = "Password"
# get this id from reschedeule page url mentioned below
appointment_id = "50249152"
appointment_url = "https://ais.usvisa-info.com/en-ca/niv/schedule/{}/appointment"
visa_locations = ["Toronto", "Ottawa", "Vancouver", "Calgary"]
```

## run(wip)
`python ./code/visa.py`