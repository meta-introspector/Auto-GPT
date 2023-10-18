import pandas as pd
import json
df = None
data = []
with open("git_samples.json") as fi:
  for l in fi:
    data.append(json.loads(l))
  df = pd.DataFrame(data)
  fig = pd.DataFrame(sorted(df["diff"].str["len"])).plot().get_figure()
  fig.savefig('diff_sizes.png')
  fig = pd.DataFrame(sorted(df["rebase_error"].str["len"])).plot().get_figure()
  fig.savefig('rebase_sizes.png')
