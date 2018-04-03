import requests


def test_server_sends_200_response():
    response = requests.get('http://127.0.0.1:3000')
    assert response.status_code == 200
    assert response.body == 'You did that thing'


def test_server_sends_404_response():
    response = requests.get('http://127.0.0.1:3000/octopus')
    assert response.status_code == 404
    assert response.body == 'Not found'


# def test_server_sends_404_response():
#     response = requests.get('http://127.0.0.1:3000/octopus')
#     assert response.status_code == 404
#     assert response.body == 'Not found'
    