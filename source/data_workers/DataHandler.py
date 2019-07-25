import operator
import os
import time
from collections import Counter

from Config import Config
from source.static.StaticData import StaticData
from source.static.StaticMethods import StaticMethods
from source.vk_api.UserAPI import UserAPI


class DataHandler:
    def __init__(self, user_id):
        self.user_id = user_id
        self.vk = UserAPI(user_id=self.user_id)
        self.cities = []
        self.schools = []
        self.univers = []
        self.repl = []

    def save(self, data):
        if not Config.save_results:
            return
        try:
            os.mkdir("./stdout/")
        except FileExistsError:
            pass
        f = open('./stdout/{}.txt'.format(self.user_id), 'w', encoding='utf-8')
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
            univer = data['university_name'].replace(',', '')
            if univer:
                self.univers.append(univer)
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
                current = ["University", self.univers]
            try:
                repl.append('\n{}:\n{}\n{}\n{}\n'.format(current[0],
                                                         '1. {}: {} ({}/{})'.format(self.repl[i][0].replace('\'', ''),
                                                                                    StaticMethods.get_percentage(
                                                                                        self.repl[i][1],
                                                                                        str(len(current[1])), 3),
                                                                                    self.repl[i][1].strip(),
                                                                                    str(len(current[1])), 3),
                                                         '2. {}: {} ({}/{})'.format(
                                                             self.repl[i + 1][0].replace('\'', ''),
                                                             StaticMethods.get_percentage(
                                                                 self.repl[i + 1][1],
                                                                 str(len(current[1])), 3),
                                                             self.repl[i + 1][1].strip(),
                                                             str(len(current[1]))),
                                                         '3. {}: {} ({}/{})'.format(
                                                             self.repl[i + 2][0].replace('\'', ''),
                                                             StaticMethods.get_percentage(
                                                                 self.repl[i + 2][1],
                                                                 str(len(current[1])), 3),
                                                             self.repl[i + 2][1].strip(),
                                                             str(len(current[1])))))
            except:
                return False

        return repl

    def handler(self):
        counter = 0
        users = self.vk.get_friends()
        StaticData.log.log(text="Got user's friends.", type_s='success')
        for user in users:
            user_info = self.vk.get_info(user)
            time.sleep(0.4)
            counter += 1
            StaticData.log.log(
                'Users handling {} ({}/{})'.format(StaticMethods.get_percentage(counter, len(users)), str(counter),
                                                   str(len(users))), type_s='log_w')
            StaticData.percent = StaticMethods.get_percentage(counter, len(users))
            self.cities_handler(user_info[0])

        data = [Counter(self.cities), Counter(self.schools), Counter(self.univers)]

        self.post_handler(data)
        out = self.reply_contruct()
        self.save(out)

        StaticData.log.log(text='\n', type_s='print')
        StaticData.log.log(text='User with ID {} handled.'.format(self.user_id), type_s='success')
        print(''.join(out))
