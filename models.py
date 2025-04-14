from dataclasses import dataclass, asdict
import json


@dataclass
class EventDate:
    date: str


@dataclass
class Event:
    summary: str
    location: str
    description: str
    end: EventDate
    start: EventDate

    def to_json(self) -> str:
        return json.dumps(asdict(self))

    def to_dict(self) -> dict:
        return asdict(self)
