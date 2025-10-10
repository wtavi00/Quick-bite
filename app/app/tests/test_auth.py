import pytest
from app import create_app
from app.models.user import db, User

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///:memory:"
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client

def test_register_login(client):
    # Test registration
    resp = client.post('/api/auth/register', json={"username": "alice", "password": "pass123"})
    assert resp.status_code == 201
    data = resp.get_json()
    assert "user_id" in data

    # Test login
    resp2 = client.post('/api/auth/login', json={"username": "alice", "password": "pass123"})
    assert resp2.status_code == 200
    data2 = resp2.get_json()
    assert "access_token" in data2
