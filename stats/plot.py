import pandas as pd
import json
import matplotlib.pyplot as plt

df = None
data = []
with open("git_samples.json") as fi:
  for l in fi:
    data.append(json.loads(l))
  df = pd.DataFrame(data)

  difflen    = pd.DataFrame(sorted(pd.to_numeric(df["diff"].str["len"])))
  difflen.to_csv("difflen.csv")
  rebase_err = pd.DataFrame(sorted(pd.to_numeric(df["rebase_error"].str["len"])))
  rebase_err.to_csv("rebase_err.csv")
  
  fig = difflen.plot().get_figure()
  fig.savefig('diff_sizes.png')
  fig = rebase_err.plot().get_figure()
  fig.savefig('rebase_sizes.png')

  plt.hist(difflen)  
  plt.savefig('diff_hist.png')
  plt.hist(rebase_err)  
  plt.savefig('rebase_hist.png')


    
  #fig = pd.DataFrame(sorted(df["rebase_error"].str["len"])).hist().get_figure()
  #fig.savefig('rebase_hist.png')
