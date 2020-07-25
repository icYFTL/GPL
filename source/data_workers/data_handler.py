import operator
import os
import time
from collections import Counter
import logging
import hues

from core import config
from source.static.static_methods import StaticMethods
from source.vk_api.user_api import UserAPI


class DataHandler:
    def __init__(self, user_id, token=None):
        self.user_id = user_id
        self.vk = UserAPI(user_id=self.user_id, token=token)
        self.cities = []
        self.schools = []
        self.high_schools = []
        self.repl = []
        self.logger = logging.getLogger('DataHandler')

    def save(self, data):
        if not config['save_results']:
            return
        try:
            os.mkdir("./stdout/")
        except FileExistsError:
            pass
        f = open(f'./stdout/{self.user_id}.txt', 'w', encoding='utf-8')
        f.write(''.join(data))
        f.close()

    def cities_handler(self, data):
        try:
            city = data['city']['title'].replace(',', '')
            if city:
                self.cities.append(city)
        except:
            pass
        self.schools_handler(data)

    def schools_handler(self, data):
        try:
            school = data['schools'][-1]['name'].replace(',', '')
            if school:
                self.schools.append(school)
        except:
            pass
        self.univers_handler(data)

    def univers_handler(self, data):
        try:
            univer = data['university_name'].replace(',', '').replace('\r\n', '')
            if univer:
                self.high_schools.append(univer)
        except:
            pass

    def post_handler(self, data):
        for i in range(len(data)):
            if len(data[i]) > 2:
                self.repl.append(str(sorted(dict(data[i]).items(), key=operator.itemgetter(1))[-1]).replace('(',
                                                                                                            '').replace(
                    ')', '').split(','))
                self.repl.append(str(sorted(dict(data[i]).items(), key=operator.itemgetter(1))[-2]).replace('(',
                                                                                                            '').replace(
                    ')', '').split(','))
                self.repl.append(str(sorted(dict(data[i]).items(), key=operator.itemgetter(1))[-3]).replace('(',
                                                                                                            '').replace(
                    ')', '').split(','))
            elif len(data[i]) > 1:
                self.repl.append(str(sorted(dict(data[i]).items(), key=operator.itemgetter(1))[-1]).replace('(',
                                                                                                            '').replace(
                    ')', '').split(','))
                self.repl.append(str(sorted(dict(data[i]).items(), key=operator.itemgetter(1))[-2]).replace('(',
                                                                                                            '').replace(
                    ')', '').split(','))
                self.repl.append("Не найдено")
            elif len(data[i]) == 1:
                self.repl.append(str(sorted(dict(data[i]).items(), key=operator.itemgetter(1))[-1]).replace('(',
                                                                                                            '').replace(
                    ')', '').split(','))
                self.repl.append("Не найдено")
                self.repl.append("Не найдено")
            else:
                self.repl.append("Не найдено")
                self.repl.append("Не найдено")
                self.repl.append("Не найдено")

    def reply_contruct(self):
        repl = []
        current = ["City", self.cities]
        for i in range(0, 9, 3):
            if i == 3:
                current = ["School", self.schools]
            if i == 6:
                current = ["University", self.high_schools]
            try:
                repl.append('\n{}:\n{}\n{}\n{}\n'.format(current[0],
                                                         '1. {}: {} ({}/{})'.format(self.repl[i][0].replace('\'', '') if
                                                                                    self.repl[
                                                                                        i] != 'Не найдено' else 'Не найдено',
                                                                                    StaticMethods.get_percentage(
                                                                                        self.repl[i][1] if self.repl[
                                                                                                               i] != 'Не найдено' else '0',
                                                                                        str(len(current[1])) if
                                                                                        self.repl[
                                                                                            i] != 'Не найдено' else '0',
                                                                                        3),
                                                                                    self.repl[i][1].strip() if
                                                                                    self.repl[
                                                                                        i] != 'Не найдено' else '0',
                                                                                    str(len(current[1])) if self.repl[
                                                                                                                i] != 'Не найдено' else '0',
                                                                                    3),
                                                         '2. {}: {} ({}/{})'.format(
                                                             self.repl[i + 1][0].replace('\'', '') if
                                                             self.repl[
                                                                 i + 1] != 'Не найдено' else 'Не найдено',
                                                             StaticMethods.get_percentage(
                                                                 self.repl[i + 1][1] if
                                                                 self.repl[
                                                                     i + 1] != 'Не найдено' else '0',
                                                                 str(len(current[1])) if
                                                                 self.repl[
                                                                     i + 1] != 'Не найдено' else '0', 3),
                                                             self.repl[i + 1][1].strip() if
                                                             self.repl[
                                                                 i + 1] != 'Не найдено' else '0',
                                                             str(len(current[1])) if
                                                             self.repl[
                                                                 i + 1] != 'Не найдено' else '0'),
                                                         '3. {}: {} ({}/{})'.format(
                                                             self.repl[i + 2][0].replace('\'', '') if
                                                             self.repl[
                                                                 i + 2] != 'Не найдено' else 'Не найдено',
                                                             StaticMethods.get_percentage(
                                                                 self.repl[i + 2][1] if
                                                                 self.repl[
                                                                     i + 2] != 'Не найдено' else '0',
                                                                 str(len(current[1])) if
                                                                 self.repl[
                                                                     i + 2] != 'Не найдено' else '0', 3),
                                                             self.repl[i + 2][1].strip() if
                                                             self.repl[
                                                                 i + 2] != 'Не найдено' else '0',
                                                             str(len(current[1])) if
                                                             self.repl[
                                                                 i + 2] != 'Не найдено' else '0')))
            except:
                return False

        return repl

    def handler(self):
        users = self.vk.get_friends()
        self.logger.info("Got user's friends")
        users_info = []
        while len(users) > 0:
            users_info.append(self.vk.get_info(users[:1000]))
            del (users[:1000])
            time.sleep(0.4)

        for user in users_info:
            for i in user:
                self.cities_handler(i)

        data = [Counter(self.cities), Counter(self.schools), Counter(self.high_schools)]

        self.post_handler(data)
        out = self.reply_contruct()
        self.save(out)

        self.logger.info(f'User with ID {self.user_id} handled')
        if not config['server_mode']:
            hues.success(''.join(out))
        else:
            return ''.join(out)

