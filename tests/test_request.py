import sys
import pytest
from dust_catcher.request import Request


@pytest.fixture
def GET():
    data = [
        b"PUT / HTTP/1.1\r\n",
        b"\r\n",
    ]

    return data


@pytest.fixture
def PUT():
    data = [
        b"PUT / HTTP/1.1\r\n",
        b"Content-Type: application/json\r\n",
        b"User-Agent: PostmanRuntime/7.29.2\r\n",
        b"Accept: */*\r\n",
        b"Postman-Token: 9835a933-e187-4071-895b-b1e67eb9be42\r\n",
        b"Host: 192.168.1.106\r\n",
        b"Accept-Encoding: gzip, deflate, br\r\n",
        b"Connection: keep-alive\r\n",
        b"Content-Length: 24\r\n",
        b"\r\n",
    ]
    return data


def test_method_is_set(PUT):
    r = Request(PUT)

    assert r.method == "PUT"


def test_headers_are_parsed(PUT):
    r = Request(PUT)

    result = dict(sorted(r.headers.items()))

    assert result == {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Content-Length": "24",
        "Content-Type": "application/json",
        "Host": "192.168.1.106",
        "Postman-Token": "9835a933-e187-4071-895b-b1e67eb9be42",
        "User-Agent": "PostmanRuntime/7.29.2",
    }
