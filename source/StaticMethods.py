class StaticMethods:
    @staticmethod
    def get_percentage(a, b):
        if ((int(a) / int(b)) * 100) < 1:
            return str(int(a) / int(b)) + '%'
        return str(int(int(a) / int(b) * 100)) + '%'
