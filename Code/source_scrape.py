import argparse
import logging
import requests

# local imports
from utils import write_json

def parse_args():
    """Function to parse command line arguments"""

    parser = argparse.ArgumentParser()
    # FIXME: switch this argument to an optional 
    parser.add_argument('-o', '--out-path', type = str, default='out.json', help = 'Path to save source info to')
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
    source_data = source[0]

    # save source info
    logging.info("Saving Source Information")
    write_json(source_data, args.out_path)
    logging.info(" ")

    return

if __name__ == "__main__":
    main()
