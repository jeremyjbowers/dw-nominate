import datetime
import os
import time

from bs4 import BeautifulSoup
import fire
import requests
import ujson as json

DATA_DIR = os.environ.get('DW_NOMINATE_DATA_DIR', '/tmp')
BASE_URL = 'https://voteview.polisci.ucla.edu/static/data/csv/party/party_all.csv'


class Party(object):
    def get(self):
        r = requests.get(BASE_URL)
        with open('%s/%s' % (DATA_DIR, BASE_URL.split('/')[-1]), 'w') as writefile:
            writefile.write(r.text)

    def parse(self, output):
        with open('%s/%s' % (DATA_DIR, BASE_URL.split('/')[-1]), 'r') as readfile:
            if output == 'csv':
                sys.stdout.write(readfile.read())
            if output == 'json':
                payload = csv.DictReader(readfile)
                sys.stdout.write(json.dumps(payload))


if __name__ == '__main__':
  fire.Fire(Party)
