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
            # NOTE: think about where the logs should be stored ...
            logging.FileHandler(f'./logs/source_download_{now}.log'),
            logging.StreamHandler()
            ]
        )

    args = parse_args()

    # scrape NFL information
    logging.info(f'Scraping Source Information for {now}')
    
    # create, build and run get data for the host
    # TODO: implement a factory pattern here to allow for easier creation of different types of hosts ... 
    # link to factory pattern here: https://realpython.com/factory-method-python/#introducing-factory-method
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
