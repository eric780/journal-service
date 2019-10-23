# Journal App
## Product Spec
A simple local app that allows viewing, editing, and adding journal entries. Everything is run on a local server with a database.
The landing page will have the following options: 
1) Search for a particular entry 
2) Add new entry
3) View all entries

### Searching for entries
**P0**
Super simple date-string lookup (format; `YYYY-MM-DD`). 
**P1**
Eventually show a calendar view with markings on which dates have entries.
**P2**
Another important aspect is keyword search. We should be able to search through all entries for keywords, and return any entries that contain them.

Optional: We can also support editing on any entry that is displayed as a result.

### Adding new entries
**P0**
Super simple new entry functionality by having the client pass in a date and some text. This will need to be safe and not allow overwrites on existing entries, or at least have some confirmation.
The editor can be a really basic text box. We can apply a line width restriction on the client side.

**P1**
We can be smart about what entries are missing (check the current date, any previous missing dates). 

### Viewing all entries
**P0**
Simplest way to render all dates and all entries.

**P1**
Nicer UI that allows for grouping by calendar view, loading most recent first, etc.

## Architecture
### Endpoints
- `get_entry(date: str) -> str`
- `add_entry(date: str, content: str) -> OK`


## Getting Started
From the /backend/ directory, run `python manage.py runserver` to start the backend service at localhost:8000

From the root directory, run `yarn start` to initialize the react app at localhost:3000