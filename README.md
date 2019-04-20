# Simple Data Science (Cookiecutter)

# Get Started 

```bash
pip3 install cookiecutter 
cookiecutter https://github.com/hayata-yamamoto/cookiecutter-data-science-for-team
```


# Structure 

```text
cookiecutter-simple-data-science/
├── docs
│   └── docs
└── {{ cookiecutter.repo_name }}
    ├── docs
    └── {{ cookiecutter.repo_name }}
        ├── data
        │   ├── interim
        │   ├── processed
        │   └── raw
        ├── modules
        ├── notebooks
        │   ├── exploratory
        │   └── predictive
        ├── src
        │   ├── core
        │   ├── datasets
        │   ├── features
        │   └── models
        └── tests
```