# report on the jc output
import click
import json
from collections import Counter
import pandas as pd

@click.command()
@click.argument('infile', type=click.File('r'))
def main(infile):
    df = pd.read_csv(infile)
    for x in df['name']:
        print(x.split(" ")[0])
if __name__ =="__main__":
    main()
