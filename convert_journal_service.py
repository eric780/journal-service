from collections import OrderedDict
from dateutil import parser
from tinydb import TinyDB, Query
from journal_model import JournalEntry
from typing import List
import constants
import glob
import os
import re
import sys

class ConvertJournalService():
    def __init__(self, db_filename):
        self.db = TinyDB(db_filename)
        # TODO cleanly handle new databases once the db becomes source of truth
        # Alternatively, let's back up to text files?
        self.db.purge()

    def convert_files(self, filenames) -> None:
        for journal_filename in filenames:
            with open(journal_filename, 'r') as journal_file:
                journal_year = journal_filename.rsplit(".txt", 1)[0]
                lines = journal_file.readlines()
                print("Processing year: ", journal_year)
                processed_entries = self.process_lines(journal_year, lines)
                # put these into DB
                self.db.insert_multiple(
                    {'date': entry.getDate(), 'entry': entry.getContent()} 
                        for (date,entry) in processed_entries.items())

        print("All values added to db!")

        # sanity check
        print("Running sanity check on database...")
        date_set = set()
        sanity_check_success = True
        for entry in self.db.all():
            if entry['date'] in date_set:
                print("Sanity check failed, duplicate entry found for: ", entry['date'])
                sanity_check_success = False
            date_set.add(entry['date'])

        if sanity_check_success:
            print("Sanity Check success. No duplicate entries.")


    def process_lines(self, year, lines) -> List[JournalEntry]:
        """
        Loop through the lines and split them into entries:
        For each line:
        - If the line is a date, wrap up old entry and start a new one
        - If EOF, wrap up old entry
        - Else append line to current entry
        """
        processed_entries = OrderedDict()
        current_date = None
        current_entry = ""
        for line in lines:
            if self.is_valid_date(line):
                # we have a valid date
                date = parser.parse(line)
    
                # flush existing
                if current_date is not None:
                    self.save_entry(processed_entries, current_date, current_entry)
                current_date = date
                current_entry = ""
    
            else:
                # not a date, so just contents
                current_entry += line
    
        # at the end, flush whatever we have
        if current_date is not None:
            self.save_entry(processed_entries, current_date, current_entry)

        return processed_entries

    def save_entry(self, processed_entries, current_date, current_entry):
        # parse into model so we can use convenience methods
        journal_entry = JournalEntry(current_date, current_entry)

        if journal_entry.getDate() in processed_entries:
            print("ERROR: duplicate date detected!", journal_entry.getDate())
            sys.exit()
        else:
            processed_entries[journal_entry.getDate()] = journal_entry

    def is_valid_date(self, line):
        return re.match('[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]\n', line)

if __name__ == "__main__":
    ConvertJournalService(constants.DB_FILENAME).convert_files(glob.glob("*.txt"))