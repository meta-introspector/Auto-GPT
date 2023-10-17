# report on the csv output and pulls the code
# `run.py filtered_result2.csv`
import click
import json
from collections import Counter
import pandas as pd

import click
import json
#pip install GitPython
from evaluate_branch import _evaluate_branch

@click.command()
@click.argument('infile', type=click.File('r'))
def main(infile):
    df = pd.read_csv(infile)
    for x in df['ref']:
        ref = ""
        if " " in x:
            ref = x.split(" ")[0]
        else:
            ref = x
            
        #print(f"git log --decorate=full ~{x}..upstream/master > {x}.txt" )
        _evaluate_branch(ref)
        #print(f"git branch -a --contains {ref} > {ref}.branch" )
            
if __name__ =="__main__":
    main()
