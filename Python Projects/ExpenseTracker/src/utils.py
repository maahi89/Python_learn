from datetime import datetime

def validate_date(date_str):
    """Validate date in YYYY-MM-DD format"""
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False
