import hues

from source.static.StaticMethods import StaticMethods


class LogsController:
    main_path = './logs/log.txt'
    record_format = '[{type}] | ({time}): {record}\n'

    def stdout(fn):  # Thanks for method template, @Tishka17 (TG);
        def wrapped(self, text, type_s):
            if type_s == 'log':
                hues.log(fn(self, text, type_s))
            elif type_s == 'warn':
                hues.warn(fn(self, text, type_s))
            elif type_s == 'error':
                hues.error(fn(self, text, type_s))
            elif type_s == 'success':
                hues.success(fn(self, text, type_s))
            elif type_s == 'success_w':
                hues.success(fn(self, text, type_s))
            elif type_s == 'log_w':
                hues.log(fn(self, text, type_s))
            elif type_s == 'print':
                print(fn(self, text, type_s))

        return wrapped

    @stdout
    def log(self, text, type_s):
        if type_s == 'log_w' or type_s == 'print' or type_s == 'success_w':
            return text
        data = LogsController.record_format.format(type=type_s, time=StaticMethods.get_time().strftime("%D %T"),
                                                   record=text)
        f = open(LogsController.main_path, 'a', encoding='utf-8')
        f.write(data)
        f.close()
        return text
