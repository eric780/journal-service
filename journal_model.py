from datetime import date

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