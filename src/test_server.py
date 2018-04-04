import requests
from . import server


def test_server_sends_200_response():
    response = requests.get('http://127.0.0.1:3000')
    assert response.status_code == 200
    assert response.body == 'You did that thing'


def test_server_sends_404_response():
    response = requests.get('http://127.0.0.1:3000/octopus')
    assert response.status_code == 404
    assert response.body == '404, This is not the page you are looking for'


def test_server_sends_msg_for_cowsay_page():
    response = requests.get('http://127.0.0.1:3000/cowsay')
    assert response.status_code == 200
    assert response.body == 

def test_server_sends_msg_for_custom_msg_page():
    response = requests.get('http://127.0.0.1:3000/cow?msg=bark')
    assert response.status_code == 200
    assert text.val == 'bark'