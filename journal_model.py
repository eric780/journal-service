from datetime import date
from dateutil import parser

class JournalEntry():
    def __init__(self, date, content):
        self.date = date
        self.content = content

    def __str__(self):
        return self._to_string()

    def __repr__(self):
        return self._to_string()

    def _to_string(self) -> str:
        return self.getDate() + "\n" + self.getContent()

    def getDate(self) -> str:
        return self.date.date().isoformat()

    def getContent(self) -> str:
        return self.content

    def from_db_entry(entry):
        return JournalEntry(parser.parse(entry['date']), entry['entry'])