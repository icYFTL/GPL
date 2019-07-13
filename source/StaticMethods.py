from datetime import datetime

import pytz


class StaticMethods:
    @staticmethod
    def get_percentage(a, b, digits=0):
        return str(StaticMethods.to_fixed(int(a) / int(b) * 100, digits)) + '%'

    @staticmethod
    def to_fixed(numObj, digits=0):
        return f"{numObj:.{digits}f}"

    @staticmethod
    def get_time():
        return datetime.now(pytz.timezone('Europe/Moscow'))
