from dataclasses import dataclass, asdict
import json


@dataclass
class EventDate:
    dateTime: str
    timeZone: str


@dataclass
class Event:
    summary: str
    location: str
    description: str
    start: EventDate
    end: EventDate

    def to_dict(self) -> dict:
        return asdict(self)
