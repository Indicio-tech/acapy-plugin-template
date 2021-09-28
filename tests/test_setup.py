"""Test setup."""
from aries_cloudagent.config.injection_context import InjectionContext
from aries_cloudagent.core.event_bus import EventBus
import pytest

import my_plugin as test_module

@pytest.fixture
def context(event_bus):
    context = InjectionContext()
    context.injector.bind_instance(EventBus, event_bus)
    yield context


@pytest.mark.asyncio
async def test_setup(context):
    await test_module.setup(context)
