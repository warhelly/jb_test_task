import credentials
import requests


def test_successful_login():
    # Test successful login with valid credentials
    data = {
        'email': credentials.LOGIN,
        'password': credentials.PASSWORD
    }
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(credentials.URL, json=data)
    assert response.status_code == 200
    assert response.text == '"OK"'


def test_failed_login():
    # Test failed login with invalid credentials
    data = {
        'email': 'fake_user',
        'password': 'wrong_password'
    }
    response = requests.post(credentials.URL, json=data)
    assert response.status_code == 200
    assert response.text == '"INCORRECT"'


def test_with_valid_cookie():
    # Test with valid cookie
    data = {
        'email': credentials.LOGIN,
        'password': credentials.PASSWORD
    }
    response = requests.post(credentials.URL, json=data)
    cookies = response.cookies
    response = requests.get(credentials.URL_GET, cookies=cookies)
    assert response.status_code == 200

    
def test_with_invalid_cookie():
    # Test with invalid cookie and request to recent activity api
    URL_INSIDE = "https://k8s.stable.on-premise.datalore.io/vfs/recent"
    invalid_cookie = {"DATALORESESSIONID": "INVALIDCOOKIE"}
    response = requests.get(URL_INSIDE, cookies=invalid_cookie)
    assert response.status_code == 403
