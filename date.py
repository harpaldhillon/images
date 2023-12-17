from datetime import datetime, date

class Date:
    def __init__(self):
        pass

    def numOfDays(self, date1, date2):
        # Parse the string to a datetime object
        datetime_object = datetime.strptime(date2, '%Y-%m-%dT%H:%M:%S.%fZ')
        # Format the datetime object to the desired output
        formatted_date = datetime_object.strftime('%Y-%m-%d')
        date_object = datetime.strptime(formatted_date, '%Y-%m-%d').date()

        difference = date1 - date_object
        return difference.days