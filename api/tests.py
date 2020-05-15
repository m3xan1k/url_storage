from time import time

from fastapi.testclient import TestClient

from api.main import app


client = TestClient(app)


def test_post_visited_links():
    data = {'links': ['http://test.ru', 'https://asdf.zx?qwer=1234',
            'jkl.nm', 'http://qwer.qwer/qwer']}
    response = client.post(url=app.url_path_for('links'), json=data)
    assert response.json() == {'status': 'ok'}


def test_post_visited_links_invalid_data():
    data = {'items': ['asdf', 'zxcv', 1234]}
    response = client.post(url=app.url_path_for('links'), json=data)
    assert response.status_code == 400


def test_post_and_get_integration():
    start = str(time())

    data1 = {'links': ['https://ya.ru', 'https://habr.com']}
    data2 = {'links': ['https://twitter.com', 'gonzoweb.io']}
    data3 = {'links': ['http://ya.ru/asdf', 'http://hexlet.io',
                       'http://habr.com?lang=ru']}
    for data in [data1, data2, data3]:
        response = client.post(url=app.url_path_for('links'), json=data)
        assert response.status_code == 201

    end = str(time())
    response = client.get(url=app.url_path_for('domains'),
                          params={'from': start, 'to': end})
    response.json() == {
        'domains': [
            'ya.ru',
            'habr.com',
            'twitter.com',
            'gonzoweb.io',
            'hexlet.io',
        ]
    }


def test_post_get_wrong_params():
    data = {'links': ['http://sadf.as']}
    client.post(url=app.url_path_for('links'), json=data)

    response = client.get(url=app.url_path_for('domains'),
                          params={'from': 12345678, 'to': 12341234})
    assert response.status_code == 400

    response = client.get(url=app.url_path_for('domains'),
                          params={'from': 'asdfasdf', 'to': 12341234})
    assert response.status_code == 400

    response = client.get(url=app.url_path_for('domains'),
                          params={'from': '', 'to': 12341234})
    assert response.status_code == 400
