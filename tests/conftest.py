import os

import pytest


@pytest.fixture(scope="session")
def requirements() -> dict:
    unsorted_requirements = ['black==19.10b0', 'Flask==1.1.2', 'Flask-Migrate==2.5.3', 'flask-restx==0.2.0',
                             'Flask-SQLAlchemy==2.4.3',
                             'gunicorn==20.0.4', 'pre-commit==2.6.0', 'psycopg2==2.8.5', 'pytest==5.4.3',
                             'pytest-cov==2.10.0',
                             'python-dotenv==0.14.0', 'SQLAlchemy==1.3.18']
    sorted_requirements = ['Flask==1.1.2', 'Flask-Migrate==2.5.3', 'Flask-SQLAlchemy==2.4.3', 'SQLAlchemy==1.3.18',
                           'black==19.10b0',
                           'flask-restx==0.2.0', 'gunicorn==20.0.4', 'pre-commit==2.6.0', 'psycopg2==2.8.5',
                           'pytest==5.4.3',
                           'pytest-cov==2.10.0', 'python-dotenv==0.14.0']
    return dict(unsorted_requirements=unsorted_requirements, sorted_requirements=sorted_requirements)

