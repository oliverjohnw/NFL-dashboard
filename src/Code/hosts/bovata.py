import dataclasses
import logging
import pandas as pd
import requests

# local import
from ._base_ import Host, NoDataError

logger = logging.getLogger(__name__)
# FIXME: move this to a config and a data file somewhere ... this should not be buried in the code somewhere ...
# also maybe try to find a way to validate that the string supplied is a valid url?
nfl_url = "https://www.bovada.lv/services/sports/event/v2/events/A/description/football/nfl"

@dataclasses.dataclass
class NFLHost(Host):
    url: str = nfl_url

    def build(self) -> None:
        # no setup required for this host
        return
    
    # NOTE: the method below could be a standalone function or a classmethod?
    def process_data(self, data):
        return data[0]['events']

    def get(self) -> pd.DataFrame:
        # TODO: wrap the request in a try-except in case there is an http error
        result = requests.get(self.url)
        logger.debug(f"Request Response: {result.status_code}")   # send the logging response to the debug file ...

        if not result.json():
            raise NoDataError('No Data Recieved from request')

        final_data = pd.DataFrame(self.process_data(result.json()))
        return raw_data





