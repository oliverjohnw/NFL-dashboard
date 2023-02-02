import argparse
import logging
import requests
import pandas as pd

# local imports
from utils import write_json
from format_helpers import parse_matchup_info

def parse_args():
    """Function to parse command line arguments"""

    parser = argparse.ArgumentParser()
    parser.add_argument('source_output_path', type = str, help = 'Path to save source info to')
    args = parser.parse_args()

    return args


def main():
    """"Main Function"""
    # Setup logger

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
    logging.info('Scraping Source Information')
    source = requests.get("https://www.bovada.lv/services/sports/event/v2/events/A/description/football/nfl").json()
    source_data = source[0]['events']
    source_data = pd.DataFrame(source_data)

    # save source info
    logging.info("Saving Source Information")
    source_data.to_csv(args.source_output_path)
    logging.info(" ")

    return

if __name__ == "__main__":
    main()
