# Simple Data Science (Cookiecutter)

# What's this?

This repository is provide minimal and useful python repository for data science project. Under {{ cookiecutter.repo_name }}, several files are written including Dockerfile, Pipfile.lock and setup.py. 

If you wanna start your project right now, this could be helpful to reduce your initial setting process. 

# Get Started 

```bash
pip3 install cookiecutter 
cookiecutter https://github.com/hayata-yamamoto/cookiecutter-simple-data-science
```


# Structure 

```text
cookiecutter-simple-data-science/
├── docs
│   └── docs
└── {{\ cookiecutter.repo_name\ }}
    ├── data
    │   ├── interim
    │   ├── processed
    │   └── raw
    ├── notebooks
    │   ├── exploratory
    │   └── predictive
    └── {{\ cookiecutter.repo_name\ }}
        ├── src
        ├── tasks
        └── tests
```
