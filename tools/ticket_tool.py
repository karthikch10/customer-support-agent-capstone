# tools/ticket_tool.py
import json, uuid, datetime, os

TICKET_DB = os.path.join("data", "tickets.json")

def _read_db():
    try:
        with open(TICKET_DB, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def _write_db(tickets):
    os.makedirs(os.path.dirname(TICKET_DB), exist_ok=True)
    with open(TICKET_DB, "w") as f:
        json.dump(tickets, f, indent=2)

def create_ticket(customer_id, subject, description, priority="medium"):
    ticket = {
        "id": str(uuid.uuid4()),
        "customer_id": customer_id,
        "subject": subject,
        "description": description,
        "priority": priority,
        "status": "open",
        "created_at": datetime.datetime.utcnow().isoformat() + "Z"
    }
    tickets = _read_db()
    tickets.append(ticket)
    _write_db(tickets)
    return ticket

def list_tickets():
    return _read_db()
