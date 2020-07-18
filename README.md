# claudio-requirements-sorter

## The way requirements files should look 

### Install
`pip install claudio_requirements_sorter`

### Usage
To use this tool simply pass the requirements file to sort as the first argument and the output file as the second argument:

`claudio_requirements_sorter requirements.txt requirements.txt`

### Example output of how the requirements will be sorted:
```
Flask==1.1.2
Flask-Migrate==2.5.3
Flask-SQLAlchemy==2.4.3
SQLAlchemy==1.3.18
black==19.10b0
flask-restx==0.2.0
gunicorn==20.0.4
pre-commit==2.6.0
psycopg2==2.8.5
pytest==5.4.3
pytest-cov==2.10.0
python-dotenv==0.14.0
```