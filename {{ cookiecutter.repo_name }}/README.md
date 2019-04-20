# {{ cookiecutter.repo_name }}
{{ cookiecutter.description }}

# Get Started 

```bash
python3 -m venv venv 
. venv/bin/activate
python3 setup.py install # or develop
```


# Structure 
```text
{{ cookiecutter.repo_name }}/
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