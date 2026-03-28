#!/usr/bin/env python3
"""
Simple EventID analyzer for a small CSV dataset.
Usage: python scripts/parse_logs.py data/sample_events.csv
"""

import csv
import sys
from collections import Counter

def parse_int(val):
    try:
        return int(val)
    except Exception:
        return None

def analyze(csv_path):
    counts = Counter()
    logon_types = Counter()
    accounts = Counter()
    hosts = Counter()

total = 0
with open(csv_path, newline='', encoding='utf-8') as f:
    # Accept common header names
    reader = csv.DictReader(f)
    for row in reader:
        total += 1
        eid = row.get('event_id') or row.get('EventID')
        if eid is not None:
            counts[eid] += 1

        acct = (row.get('account') or row.get('Account'))
        if acct:
            accounts[acct] += 1

        host = (row.get('host') or row.get('Host'))
        if host:
            hosts[host] += 1

        ltype = (row.get('logon_type') or row.get('LogonType'))
        if ltype:
