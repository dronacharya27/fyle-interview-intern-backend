from core.libs.exceptions import FyleError
def test_exceptions():
    flye_error = FyleError(status_code=400, message='test message')

    test_dict = {'message':'test message'}
    assert flye_error.to_dict() == test_dict


def test_app(client):
    response = client.get(
        '/',
    )

    assert response.status_code == 200

    
    assert response.json['status'] == 'ready'


    
   