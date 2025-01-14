import pytest
from rest_framework.test import APIClient

from tests.entities import AuthorizedUser


@pytest.mark.parametrize(
    'hello_world_query, hello_world_header',
    [
        ('', None),
        ('?hello_world', 'Hello, World!'),
    ],
)
def test_interceptor_headers(hello_world_query, hello_world_header):
    client = APIClient()
    user = AuthorizedUser()
    client.force_authenticate(user)
    url = f'/winter-simple/get/{hello_world_query}'
    response = client.get(url)
    assert response.get('x-method') == 'SimpleAPI.get'
    assert response.get('x-hello-world') == hello_world_header
