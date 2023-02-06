# Usage

## Purpose

This document will detail the usage instructions for this application.

__NOTE__: All runnable scripts should be run as a module which will keep relative imports consistent. The directory to launch any supported script from will be the src/code folder. Furthermore you can move to that directory then call python like:

```
python -m path.to.runnable.script
```

Notice that the file path is separated by . instead of a / and also the script is called without the .py extension. For more details on scripts vs module see [here](https://realpython.com/run-python-scripts/#how-to-run-python-scripts-using-the-command-line) and [here](https://stackoverflow.com/questions/22241420/execution-of-python-code-with-m-option-or-not) for a quick stack overflow summary.

### Currently

There is currently one supported script (Code/source_scrape.py) which can be run from the terminal (again from the code folder in src):

```
python -m scrape_data
```

## Note on logging

Logging is supported in python and is useful. Remember there is shell redirection which allows sending the output and error info from the script to a file at runtime. I am not sure which is the best method nor the performance of either. 

Here is an example of shell redirection:

```
python -m source_scrape > thing.txt 2>&1
```

The command above will send all the info (output and error) to a text file.txt. The logging info will still be written to the file configured in python as well in this case. 
