from app import app

def test_hello():
    """Tests the hello endpoint."""
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b"Hello, DevSecOps!"