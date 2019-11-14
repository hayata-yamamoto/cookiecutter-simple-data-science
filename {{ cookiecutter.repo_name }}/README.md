# {{ cookiecutter.repo_name }}
{{ cookiecutter.description }}

# Get Started 

```bash
$ pip3 install pipenv # if necessary
$ pipenv --python 3.7 && pipenv sync --dev && pipenv run develop
```


# Structure 
```text
{{ cookiecutter.repo_name }}
├── data
│   ├── interim
│   ├── processed
│   └── raw
├── notebooks
│   ├── exploratory
│   └── predictive
└── {{ cookiecutter.repo_name }}
    ├── src
    ├── tasks
    └── tests
```
