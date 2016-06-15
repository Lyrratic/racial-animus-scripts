#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse

__author__='Lucy Shen'

"""
Simple script to check if gtrends sample outputs are identical.

Example command-line call: python check_sample_equal.py directory/name'
"""

def main(keywords):
    google_username = "lshen.api@gmail.com"
    google_password = "googletrends"
    path = "data/"
    # regions = ['US-AK-743', 'US-AK-745', 'US-AK-747']
    regions = ['US-AK-743']
    sample_counter = 1
    timeframe = '01/2004 48m' # Jan 2004 to Dec 2007

    # connect to Google
    connector = pyGTrends(google_username, google_password)

    print "connected"

    # make request
    for region in regions:
        while sample_counter < 10:
            connector.request_report(keywords, hl='en-US', geo=region, date=timeframe)
            print "waiting..."
            time.sleep(randint(5, 10))
            print "saving..."
            # download file
            connector.save_csv(path, region + '_' + str(sample_counter))
            print "done with iteration", sample_counter
            sample_counter += 1

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("keyword", help="Search keywords, separated by a comma and a space", type=str)

    args = parser.parse_args()

    main(args.keyword)
