import csv
import datetime
import os
import time
import sys

from bs4 import BeautifulSoup
import fire
import requests
import ujson as json

DATA_DIR = os.environ.get('DW_NOMINATE_DATA_DIR', '/tmp')
BASE_URL = 'https://voteview.polisci.ucla.edu/static/data/csv/%s/%s_%s_%s.csv'


class DWNOM(object):
    def get(self, data_type, house, term):
        r = requests.get(BASE_URL % (data_type, data_type, house, term))
        with open('%s/%s_%s_%s.csv' % (DATA_DIR, data_type, house, term), 'w') as writefile:
            writefile.write(r.text)

    def parse(self, data_type, house, term, output):
        with open('%s/%s_%s_%s.csv' % (DATA_DIR, data_type, house, term), 'r') as readfile:
            if output == 'csv':
                sys.stdout.write(readfile.read())
            if output == 'json':
                payload = csv.DictReader(readfile)
                sys.stdout.write(json.dumps(payload))


if __name__ == '__main__':
  fire.Fire(DWNOM)
