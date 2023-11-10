
# most common edited files

```
python report.py all.json 
```

That produces user_files.csv

```
cut -d, -f3 user_files.csv  |sort |uniq -c | sort -n > mostcommon.txt

```



# 30k checkout steps

`../forks.py` produces a list of forks
cut "-d'" -f4 forks.txt > forks2.txt
`for x in `cat forks2.txt`; do git remote add $(echo $x| cut -d/ -f1 ) https://github.com/$x; done; `

I shared by .git/config with the 30k remotes
to use you can copy data/config into .git/config 


run jobs in 100 parallel
`cat todo.txt | parallel -j 100 -v`


# rebase 
`for x in `cat arena/todo.txt `; do git rebase --abort; git checkout $x; git rebase origin/master ; git diff origin/master > rebase/$x.txt; git rebase --abort; done`


# tool to fetch out the git sha from the results

`python ./run.py filtered_result2.csv > todo.txt`

get the logs for the past 30 days
`jc git log --all --stat --since 2023-09-01 --decorate=full | jq > all_30.json`


# look at the shortlist
for x in `cat short_list_todo.txt `; do echo $x; git log --decorate=full $x -1; done > 
grep ref shortlist.txt  >shortrefs.txt
