# Simple Data Science (Cookiecutter)

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