from uuid import uuid4

from bsubio.api_client import ApiClient


class _DummyPool:
    def __init__(self) -> None:
        self.cleared = False

    def clear(self) -> None:
        self.cleared = True


class _DummyRestClient:
    def __init__(self) -> None:
        self.pool_manager = _DummyPool()


def test_api_client_context_clears_pool() -> None:
    client = ApiClient()
    client.rest_client = _DummyRestClient()

    with client:
        pass

    assert client.rest_client.pool_manager.cleared is True


def test_sanitize_for_serialization_handles_uuid() -> None:
    client = ApiClient()
    uid = uuid4()

    assert client.sanitize_for_serialization(uid) == str(uid)
