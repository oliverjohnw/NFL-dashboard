import json
import os.path as osp
import pathlib

def read_json(*paths) -> dict:
    """
    Function to read a simple json file

    Parameters
    ----------
    paths : list[str]
        path to the file of interest
    
    Returns
    -------
    data : dict[str, Any]
    """
    path = pathlib.Path().joinpath(*paths)

    with open(path, 'r') as fp:
        data = json.load(fp)

    return data


def write_json(data: dict, *args, indent:int = 4, **kwargs) -> None:
    """
    Function to write a dictionary out to a json file --- according to the json standards, the dictionary keys must be strings
    Parameters 
    ----------
    data : dict
        dictionary to be written to a json file
    args : str
        path for the file to be written to
    kwargs : dict
        additional keyword arguments to json.dump

    Returns
    -------
    """
    out_path = osp.join(*args)

    with open(out_path, 'w') as fp:
        json.dump(data, fp, indent=indent, **kwargs)

    return

def read_json(opt_path):
    """
    Function to load a json file as a dictionary
    Parameters
    ----------
    args: List[str]
        input path to the json file to be read, separate arguments will be combined in to a single path: ie foo, bar, test.json -> foo/bar/test.json    
    Returns
    -------
    data: Dict[str, ?]
        json file as a dictionary
    """
    path = osp.join(opt_path)
    with open(path, 'r') as f:
        data = json.load(f)
    return data