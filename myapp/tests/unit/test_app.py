import pytest


@pytest.mark.parametrize("route", ["/", "/about", "/summariser", "/sentiment",
                                   "/subjectivity", "/readability"])
def test_web_pages(client, route):
    res = client.get(route)
    assert res.status_code == 200