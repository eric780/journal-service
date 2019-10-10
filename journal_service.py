from tinydb import TinyDB, Query
from journal_model import JournalEntry
import constants

class JournalService():
    def __init__(self):
        self.db = TinyDB(constants.DB_FILENAME)

    def get_entry(self, date) -> JournalEntry:
        Entry = Query()
        return self.db.search(Entry.date == date)

if __name__ == "__main__":
    journal_service = JournalService()
    documents = journal_service.get_entry("2016-01-10")
    if len(documents) > 0:
        test_entry = JournalEntry.from_db_entry(documents[0])
        print(test_entry)