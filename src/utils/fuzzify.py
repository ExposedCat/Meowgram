import datetime

HOUR_MIN = "%I∶%M %p"
WEEK_DAY = "%a"
MONTH_DAY = "%b %d"


class Fuzzify:

    # TODO make this adapt with military time

    @staticmethod
    def _convert_to_utc(date):
        return date.replace(tzinfo=datetime.timezone.utc).astimezone()

    @staticmethod
    def _get_difference_from_now(date):
        today = datetime.datetime.now().astimezone()
        return (today - date).days

    @staticmethod
    def dialog_last_message(date):
        date = Fuzzify._convert_to_utc(date)
        diff_from_now = Fuzzify._get_difference_from_now(date)

        if diff_from_now < 1:
            format_string = HOUR_MIN  # 08:57 AM
        elif 1 <= diff_from_now < 7:
            format_string = WEEK_DAY  # Fri
        elif diff_from_now >= 7:
            format_string = MONTH_DAY  # Apr 08

        return date.strftime(format_string)

    @staticmethod
    def message_time_sent(date):
        date = Fuzzify._convert_to_utc(date)
        diff_from_now = Fuzzify._get_difference_from_now(date)

        if diff_from_now < 1:
            format_string = HOUR_MIN  # 08:57 AM
        elif 1 <= diff_from_now < 7:
            format_string = f"{WEEK_DAY} at {HOUR_MIN}"  # Fri at 08:57 AM
        elif diff_from_now >= 7:
            format_string = f"{MONTH_DAY} at {HOUR_MIN}"  # Apr 08 at 08:57 AM

        return date.strftime(format_string)

    @staticmethod
    def dialog_last_active(date):
        date = Fuzzify._convert_to_utc(date)
        diff_from_now = Fuzzify._get_difference_from_now(date)

        if diff_from_now < 1:
            format_string = f"at {HOUR_MIN}"  # at 08:57 AM
        elif 1 <= diff_from_now < 2:
            format_string = f"yesterday at {HOUR_MIN}"  # yesterday at 08:57 AM
        elif 2 <= diff_from_now < 7:
            format_string = f"{WEEK_DAY} at {HOUR_MIN}"  # Fri at 08:57 AM
        elif diff_from_now >= 7:
            format_string = f"{MONTH_DAY} at {HOUR_MIN}"  # Apr 08 at 08:57 AM

        return date.strftime(f"last seen {format_string}")
