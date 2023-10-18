import pandas as pd
import json
import matplotlib.pyplot as plt
from git import Repo
from git.cmd import GitCommandError


repo = Repo("..")

df = None
data = []
with open("git_samples.json") as fi:
  for l in fi:
      d = json.loads(l)
      if int(d['diff']['len']) +int(d['rebase_error']['len'])> 500:
          branches = repo.git.branch("-r","--all","--contains", d['ref'])
          parts = branches.split("/")
          remote = repo.git.remote("get-url",parts[1])
          #print(parts[1],parts[2],)
          #print(f"git submodule  add {remote} {parts[1]} && cd {parts[1]} &&git checkout {parts[1]}")
          print(f"git submodule  add {remote} {parts[1]}")
          #print(parts)
          print(f"pushd {parts[1]} && git checkout {parts[2]} && popd")
