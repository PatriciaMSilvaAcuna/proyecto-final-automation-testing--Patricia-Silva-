import pytest

@pytest.fixture
def posts_data():
    return {
        "title": "Mi Pimer Posteo",
        "body": "Contindo de mi primer post",
        "userId": 1
    }


@pytest.fixture
def users_data():
    return{
        "name": "Patito",
        "username": "PatitoPms",
        "email":"pms@gmail.com"

    }

def pytest_html_report_title(report):
    report.title ="API JSONPLACEHOLDER - POST - USERS"