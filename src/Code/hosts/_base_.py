import abc
import pandas as pd

"""
This will be an abstract base class for a host (place to get data from)

The interface will contain two methods:

1. build: this method will call any setup require before fetching data
2. get: this method will fetch data from somewhere and should return a dataframe
"""

# NOTE: since this is a fairly simple api, it can probably be done via protocol but don't worry about it for now ...

class Host:
    @abc.abstractmethod
    def build(self, *args, **kwargs) -> None:
        """Function to prep the host to fetch data"""

    @abc.abstractmethod
    def get(self, *args, **kwargs) -> pd.DataFrame:
        """Function to get data from the host and process it into a dataframe"""

