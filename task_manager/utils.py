import datetime

def validate_title(title):
    if not title or not title.strip():
        raise ValueError("Title cannot be empty.")
    return title.strip()

def validate_priority(priority):
    if not priority or not priority.strip():
        return "Low"
    priority = priority.strip().title()
    if priority not in ["Low", "Medium", "High"]:
        raise ValueError("Priority must be Low, Medium, or High.")
    return priority

def validate_date(date_str):
    if not date_str or not date_str.strip():
        return None
    try:
        return datetime.datetime.strptime(date_str.strip(), "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Invalid date format. Use YYYY-MM-DD.")

def validate_status(status):
    if not status or not status.strip():
        return "Pending"
    status = status.strip().title()
    if status not in ["Pending", "In Progress", "Completed"]:
        raise ValueError("Status must be Pending, In Progress, or Completed.")
    return status
