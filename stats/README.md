* # 🌟 AutoGPT Hackathon reports

1. `cp .env.example .env`
2. edit .env add in you pat
3. `python forks.py Significant-Gravitas AutoGPT | tee forks.json`
stop when you want to , I am updating this every day now.

4. extract the reponame
cat  forks.json  | jq -r .nameWithOwner | sort -u > repos.txt

```
for x in `cat repos.txt`; do git remote add $(echo $x| cut -d/ -f1 ) https://github.com/$x; done
```

now fetch them

```
for x in `cat repos.txt`; do git fetch $(echo $x| cut -d/ -f1 ); done
```

or in parallel
``
for x in `cat repos.txt`; do echo git fetch $(echo $x| cut -d/ -f1 ); done  | parallel -j 50
``

Now we pull in the changes since sept
```
ojc git log --all --stat --since 2023-09-01 --decorate=full | jq > all_30.json
```
