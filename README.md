# dw-nominate
A Python library for downloading and parsing DW-NOMINATE files for legislators, votes and parties.

## Usage
```
python dwnom.py get <VOTE_TYPE> <HOUSE> <TERM>
python dwnom.py parse <VOTE_TYPE> <HOUSE> <TERM> <OUTPUT_FORMAT>
```

### Examples
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
