import pytest
from aries_cloudagent.core.event_bus import MockEventBus

@pytest.fixture
def event_bus():
    yield MockEventBus()
