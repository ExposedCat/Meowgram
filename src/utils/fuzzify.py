import datetime


class Fuzzify:

    # TODO make this adapt with military time

    @staticmethod
    def _convert_to_utc(date):
        return date.replace(tzinfo=datetime.timezone.utc).astimezone()

    def _get_difference_from_now(date):
        today = datetime.datetime.now().astimezone()
        return (today - date).days

    def dialog_last_message(date):
        date = Fuzzify._convert_to_utc(date)
        diff_from_now = Fuzzify._get_difference_from_now(date)

        if diff_from_now < 1:
            format_string = '%I∶%M %p'  # 08:57 AM
        elif 1 <= diff_from_now < 7:
            format_string = '%a'  # Fri
        elif diff_from_now >= 7:
            format_string = '%b %d'  # Apr 08

        return date.strftime(format_string)

    def message_time_sent(date):
        date = Fuzzify._convert_to_utc(date)
        diff_from_now = Fuzzify._get_difference_from_now(date)

        if diff_from_now < 1:
            format_string = '%I∶%M %p'  # 08:57 AM
        elif 1 <= diff_from_now < 7:
            format_string = '%a at %I∶%M %p'  # Fri at 08:57 AM
        elif diff_from_now >= 7:
            format_string = '%b %d at %I∶%M %p'  # Apr 08 at 08:57 AM

        return date.strftime(format_string)

    def dialog_last_active(date):
        date = Fuzzify._convert_to_utc(date)
        diff_from_now = Fuzzify._get_difference_from_now(date)

        if diff_from_now < 1:
            format_string = 'at %I∶%M %p'  # at 08:57 AM
        elif 1 <= diff_from_now < 2:
            format_string = 'yesterday at %I∶%M %p'  # yesterday at 08:57 AM
        elif 2 <= diff_from_now < 7:
            format_string = '%a at %I∶%M %p'  # Fri at 08:57 AM
        elif diff_from_now >= 7:
            format_string = '%b %d at %I∶%M %p'  # Apr 08 at 08:57 AM

        return date.strftime(f"last seen {format_string}")
