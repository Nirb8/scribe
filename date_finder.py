import datetime

def get_current_date_yyyy_mm_dd():
    return datetime.date.today().strftime('%Y-%m-%d')
def get_current_daily_note_filename():
    return f"{get_current_date_yyyy_mm_dd()}.md"
def get_message_to_tomorrow_title():
    tomorrow = datetime.date.today() + datetime.timedelta(1)
    tomorrow_string = tomorrow.strftime('%Y-%m-%d')
    return f"Message to Tomorrow [[{tomorrow_string}]]: "
    