import pytest

from sanic.response import text


class TestApplication(object):

    @pytest.fixture
    def sanic_view(self):
        def view(request):
            return text("Hello World!")
        return view

    @pytest.mark.parametrize('methods', [
        ['GET'], ['GET', 'POST'], ['GET', 'PUT'], ['GET', 'POST', 'PUT']
    ])
    def test_view(self, application, sanic_view, methods):
        url = '/hello'
        application.add_route(sanic_view, url, methods=methods)
        client = application.test_client

        for method in methods:
            client_method = getattr(client, method.lower())
            resp = client_method(url, gather_request=False)

            assert resp.status == 200
            assert resp.body == b"Hello World!"
