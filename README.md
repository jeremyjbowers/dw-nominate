# dw-nominate
A Python library for downloading and parsing DW-NOMINATE files for legislators, votes and parties.

## Install
```
mkvirtualenv dwnom && git clone git@github.com:jeremyjbowers/dw-nominate.git
cd dwnom && pip install -r requirements.txt
```

## Usage

### Votes and Legislators
```
python dwnom.py get <VOTE_TYPE> <HOUSE> <SESSION>
python dwnom.py parse <VOTE_TYPE> <HOUSE> <SESSION> <OUTPUT_FORMAT>
```

* Download rollcall votes for the 115th Senate as JSON.
```
python dwnom.py get rollcall senate 115
python dwnom.py parse rollcall senate 115 json
```

* Download member votes for the 112th House of Representatives as CSV.
```
python dwnom.py get member house 112
python dwnom.py parse member house 112 json
```

* Download rollcall votes for the 110th Congress (both houses) as JSON.
```
python dwnom.py get rollcall both 110
python dwnom.py parse rollcall both 110 json
```

### Parties
* Download party data as CSV and JSON.
```
python party.py get party
python party.py parse party csv
python party.py parse party json
```
