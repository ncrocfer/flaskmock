import datetime

def test_list_sources(client):
    resp = client.get('/sources')
    assert resp.json == []


def test_create_source(client, mocker):

    # Following does not work
    mock = mocker.MagicMock(return_value='123e4567-e89b-12d3-a456-426655440000')
    mocker.patch('myproject.models.get_uuid', mock)
    mock = mocker.MagicMock(return_value=datetime.datetime(2019, 1, 1))
    mocker.patch('myproject.models.get_now', mock)

    resp = client.post('/sources', json={'name': 'My source'})
    assert resp.json == {
        'name': 'My source',
        'id': '123e4567-e89b-12d3-a456-426655440000',
        'createdAt': 'Tue, 01 Jan 2019 00:00:00 GMT',
        'updatedAt': 'Tue, 01 Jan 2019 00:00:00 GMT'
    }
