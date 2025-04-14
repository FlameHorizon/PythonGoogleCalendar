from models import Event, EventDate
from datetime import datetime, timedelta


class Parser:
    def get_events(file):
        content = None
        with open(file, 'r') as f:
            content = f.readlines()

        # First line contains date
        date = content[0].replace('# ', '').strip()

        events = []
        for line in content[2:]:

            if line == '\n':
                continue

            if '=' in line:
                break

            # __import__('pprint').pprint(line)
            split = line.split(', ')

            title = split[0].replace('- ', '')
            time = split[1]
            duration = int(split[2].replace(' min', '').strip())

            combined = f"{date} {time}"
            dt = datetime.strptime(combined, '%Y-%m-%d %H:%M')
            end = dt + timedelta(minutes=duration)

            event = Event(
                summary=title,
                description=title,
                location='',
                start=EventDate(dateTime=dt.strftime(
                    "%Y-%m-%dT%H:%M:%S"), timeZone='Europe/Warsaw'),
                end=EventDate(dateTime=end.strftime(
                    "%Y-%m-%dT%H:%M:%S"), timeZone='Europe/Warsaw')
            )

            events.append(event)

        return events
