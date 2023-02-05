import pandas as pd

def parse_matchup_info(source_info: dict):
    """
    Function to create a dictionary of weekly matchups
    Parameters 
    ----------
    source_info : dict
        dictionary containing source information

    Returns
    -------
    matchups_dict : dict
        dictionary of weekly matchups and all betting info
    """

    matchups_dict = dict()

    for i in range(len(source_info['events'])):
        # matchups
        matchup = source_info['events'][i]['description']
        # matchup information
        info = source_info['events'][i]['displayGroups'][0]['markets']
        matchups_dict[matchup] = info

    return matchups_dict


