from nose.tools import *
from app import app
from tests.tools import assert_response

client = app.test_client()
client.testing = True

def test_index():
    global client
    resp = client.get('/')
    assert_response(resp, status=302)

    resp = client.get('/game')
    assert_response(resp)

    resp = client.post('/game')
    assert_response(resp, contains="You Died!")

    testdata = {'userinput': 'tell a joke'}
    resp = client.post('/game', data=testdata)
    assert_response(resp, contains="Laboratory Door")

    testdata = {'userinput': '132'}
    resp = client.post('/game', data=testdata)
    assert_response(resp, contains="Robot TRex")
