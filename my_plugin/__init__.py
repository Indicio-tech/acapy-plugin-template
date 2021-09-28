"""ACA-Py Event to Kafka Bridge."""

import re
from aries_cloudagent.config.injection_context import InjectionContext
from aries_cloudagent.core.event_bus import Event, EventBus
from aries_cloudagent.core.profile import Profile

async def setup(context: InjectionContext):
    """Setup the plugin."""
    bus = context.inject(EventBus)
    assert bus
    bus.subscribe(re.compile("acapy::.*"), example_event_handler)


async def example_event_handler(profile: Profile, event: Event):
    """Handle an event."""
    print("Event received on profile:", profile)
    print("Event:", event)
