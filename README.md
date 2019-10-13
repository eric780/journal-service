# Journal App
## Product Spec
A simple local app that allows viewing, editing, and adding journal entries. Everything is run on a local server with a database.
The landing page will have two options: 1) Search for a particular entry 2) Add new entry.
### Searching for entries
To start off, we can do a super simple date-string lookup (format; `YYYY-MM-DD`). 
To expand on date searching, we can eventually show a calendar view with markings on which dates have entries.
Another important aspect is keyword search. We should be able to search through all entries for keywords, and return any entries that contain them.

We can also support editing on any entry that is displayed as a result.
### Adding new entries
To start off, we can do super simple new entry functionality by having the client pass in a date and some text. This will need to be safe and not allow overwrites on existing entries.
The editor can be a really basic text box. We can apply a line width restriction on the client side.

To expand on this, we can be smart about what entries are missing (check the current date, any previous missing dates). 
## Architecture
### Endpoints
- `get_entry(date: str) -> str`
- `add_entry(date: str, content: str) -> OK`