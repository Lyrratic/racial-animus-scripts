#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import csv

__author__='Lucy Shen'

"""
One-time use: script to generate Google Trends-specific DMA codes for all regions in the US from a file with rows of duplicates, where the format is <Country code>-<State abbreviation>-<DMA number>. Ex: US-AK-743.

Input a CSV file in format: region name, unique DMA code. May have duplicates.
Outputs a CSV file in format: unique DMA code, state abbreviation.

Alternatively, can alter this to save and pickle a dictionary.

Command-line call: python generate_dma_codes.py docs/dma_regioncodes.csv docs/dma_regioncodes_CLEANED.csv
"""

def main(file_in, file_out):
    output_dict = {}

    # Read the file into a dictionary
    with open(file_in, mode='r') as infile:
        reader = csv.reader(infile)
        for region, code in reader:
            if code not in output_dict:
                parts = region.split(",")
                print len(parts)
                if len(parts) > 2:
                    output_dict[code] = region # will manually correct
                else:
                    state = region.split(",")[-1].strip()
                    print state
                    output_dict[code] = state
                

    # Save the dictionary to a CSV
    with open(file_out, mode='w') as outfile:
        writer = csv.writer(outfile)
        for key, value in output_dict.items():
            writer.writerow([key, value])
    

if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("infile", help="CSV file containing DMA codes, each line in format (DMA region name, DMA region code).", type=str)
    parser.add_argument("outfile", help="Destination of cleaned CSV.", type=str)

    args = parser.parse_args()

    main(args.infile, args.outfile)
