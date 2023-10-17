* # 🌟 AutoGPT Hackathon reports

1. `cp .env.example .env`
2. edit .env add in you pat
3. `python forks.py | tee forks.json`
stop when you want to 

4. extract the reponame
cat  forks.json  | jq -r .nameWithOwner > repos.txt

```
for x in `cat repos.txt`; do git remote add $(echo $x| cut -d/ -f1 ) https://github.com/$x; done
```

now fetch them

```
for x in `cat repos.txt`; do git fetch $(echo $x| cut -d/ -f1 ); done
```
