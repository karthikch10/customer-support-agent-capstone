# src/orchestrator.py
from tools.ticket_tool import create_ticket

def handle_user_message(user_id, message):
    """
    Minimal orchestrator stub. Replace classifier/retriever/resolver with real modules later.
    Returns a dict with answer, intent, and optional ticket.
    """
    # very simple rule-based intent detection for MVS:
    text = message.lower()
    if any(word in text for word in ["reset", "password", "how do i", "how to"]):
        intent = "faq"
    elif any(word in text for word in ["charged", "billing", "payment", "invoice"]):
        intent = "billing"
    elif any(word in text for word in ["crash", "error", "bug", "not working", "can't login", "cant login"]):
        intent = "technical"
    elif any(word in text for word in ["locked", "fraud", "scam", "stolen"]):
        intent = "escalate"
    else:
        intent = "other"

    if intent == "faq":
        return {"answer": "Sample FAQ response (replace with LLM output).", "intent": intent}
    elif intent == "escalate":
        ticket = create_ticket(user_id, "Escalation: issue reported", message, priority="high")
        return {"answer": f"Created ticket {ticket['id']}. Our team will follow up.", "intent": intent, "ticket": ticket}
    else:
        # For other intents, just return a placeholder
        return {"answer": "We received your message and will respond shortly.", "intent": intent}
