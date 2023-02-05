import argparse
import datetime
import logging
import requests
import pandas as pd

# local imports
from utils import write_json
from format_helpers import parse_matchup_info
from hosts.bovata import NFLHost

def parse_args():
    """Function to parse command line arguments"""

    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--out-path', type=str, default='out.json', help='Path to save source info to')
    args = parser.parse_args()

    return args


def main():
    """"Main Function"""
    # Setup logger
    now = datetime.datetime.now().date()

    formatstr = '%(asctime)s: %(levelname)s: %(funcName)s Line: %(lineno)d %(message)s'
    datestr = '%m/%d/%Y %H:%M:%S'
    logging.basicConfig(
        level=logging.INFO, 
        format=formatstr, 
        datefmt=datestr, 
        handlers=[
            logging.FileHandler('./logs/source_download.log'),
            logging.StreamHandler()
            ]
        )

    args = parse_args()

    # scrape NFL information
    logging.info(f'Scraping Source Information for {now}')
    
    # create, build and run get data for the host
    host = NFLHost()
    host.build()
    source_data = host.get()

    # save source info
    logging.info("Saving Source Information")
    source_data.to_csv(args.source_output_path)
    logging.info("Download Finished")


    return

if __name__ == "__main__":
    main()
