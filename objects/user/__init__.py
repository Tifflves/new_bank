from datetime import datetime

def time_now():
    return datetime.now().replace(microsecond=0)
