# report on the csv output and pulls the code
# `run.py filtered_result2.csv`
import click
import json
from collections import Counter
import pandas as pd

@click.command()
@click.argument('infile', type=click.File('r'))
def main(infile):
    df = pd.read_csv(infile)
    for x in df['name']:
        ref = ""
        if " " in x:
            ref = x.split(" ")[0]
        else:
            ref = x
            
        #print(f"git log --decorate=full ~{x}..upstream/master > {x}.txt" )
        print(f"python ./evaluate_branch.py {ref}")
        #print(f"git branch -a --contains {ref} > {ref}.branch" )
            
if __name__ =="__main__":
    main()
