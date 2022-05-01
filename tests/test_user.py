from flask import url_for


def test_user_home(client):
    assert client.get(url_for("user.home")).status_code == 302


def test_user_register(client):
    assert client.get(url_for("user.register")).status_code == 200


def test_user_login(client):
    assert client.get(url_for("user.login")).status_code == 200


def test_user_logout(client):
    assert client.get(url_for("user.logout")).status_code == 302
