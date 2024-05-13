import pytest
from pinaple_framework import PineAppleFrame


@pytest.fixture
def app() -> PineAppleFrame:
    return PineAppleFrame()


@pytest.fixture
def test_client(app):
    return app.test_session()
