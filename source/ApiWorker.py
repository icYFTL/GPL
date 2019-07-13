import operator
import os
import time
from collections import Counter

import vk_api

from Config import Config
from source.StaticData import StaticData
from source.StaticMethods import StaticMethods


class ApiWorker:

    def __init__(self, token, user_id):
        self.token = token
        self.user_id = user_id
        self.session = None

    def get_session(self):
        try:
            self.session = vk_api.VkApi(token=self.token)
        except:
            StaticData.log.log(text='Bad access token.', type_s='error')
            exit()

    def get_friends(self):
        self.get_session()
        try:
            return self.session.method('friends.get', {'user_id': self.user_id}).get('items')
        except:
            return False

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

    def get_info(self):
        cities = []
        schools = []
        univers = []
        repl = []
        counter = 0
        users = self.get_friends()
        StaticData.log.log(text="Got user's friends.", type_s='success')
        for user in users:
            user_info = self.session.method('users.get', {'user_ids': user, 'fields': 'city,schools,education'})
            time.sleep(0.4)
            counter += 1
            StaticData.log.log(
                'Users handled {} ({}/{})'.format(StaticMethods.get_percentage(counter, len(users)), str(counter),
                                                  str(len(users))), type_s='log_w')
            try:
                cities.append(user_info[0].get('city').get('title')).replace(',', '')
            except:
                pass
            try:
                schools.append(user_info[0].get('schools')[-1].get('name')).replace(',', '')
            except:
                pass
            try:
                univer = user_info[0].get('university_name').replace(',', '')
                if univer:
                    univers.append(univer)
            except:
                pass
        data = [Counter(cities), Counter(schools), Counter(univers)]
        top_cities = [None] * 3
        for i in range(len(data)):
            if len(data[0]) > 2:
                top_cities[0] = str(sorted(dict(data[i]).items(), key=operator.itemgetter(1))[-1]).replace('(',
                                                                                                           '').replace(
                    ')', '').split(',')
                top_cities[1] = str(sorted(dict(data[i]).items(), key=operator.itemgetter(1))[-2]).replace('(',
                                                                                                           '').replace(
                    ')', '').split(',')
                top_cities[2] = str(sorted(dict(data[i]).items(), key=operator.itemgetter(1))[-3]).replace('(',
                                                                                                           '').replace(
                    ')', '').split(',')
            elif len(data[0]) > 1:
                top_cities[0] = str(sorted(dict(data[i]).items(), key=operator.itemgetter(1))[-1]).replace('(',
                                                                                                           '').replace(
                    ')', '').split(',')
                top_cities[1] = str(sorted(dict(data[i]).items(), key=operator.itemgetter(1))[-2]).replace('(',
                                                                                                           '').replace(
                    ')', '').split(',')
            elif len(data[0]) == 1:
                top_cities[0] = str(sorted(dict(data[i]).items(), key=operator.itemgetter(1))[-1]).replace('(',
                                                                                                           '').replace(
                    ')', '').split(',')

            else:
                top_cities = 'Not found'
            try:
                if i == 0:
                    repl.append('\nCity:\n{}\n{}\n{}'.format(
                        '{}: {} ({}/{})'.format(top_cities[0][0].replace('\'', ''),
                                                StaticMethods.get_percentage(top_cities[0][1], str(len(cities)), 3),
                                                top_cities[0][1].strip(), str(len(cities)), 3),
                        '{}: {} ({}/{})'.format(top_cities[1][0].replace('\'', ''),
                                                StaticMethods.get_percentage(top_cities[1][1], str(len(cities)), 3),
                                                top_cities[1][1].strip(), str(len(cities))),
                        '{}: {} ({}/{})'.format(top_cities[2][0].replace('\'', ''),
                                                StaticMethods.get_percentage(top_cities[2][1], str(len(cities)), 3),
                                                top_cities[2][1].strip(), str(len(cities)))))
                elif i == 1:
                    repl.append('\n\nSchool:\n{}\n{}\n{}'.format(
                        '{}: {} ({}/{})'.format(top_cities[0][0].replace('\'', ''),
                                                StaticMethods.get_percentage(top_cities[0][1], str(len(cities)), 3),
                                                top_cities[0][1].strip(), str(len(cities))),
                        '{}: {} ({}/{})'.format(top_cities[1][0].replace('\'', ''),
                                                StaticMethods.get_percentage(top_cities[1][1], str(len(cities)), 3),
                                                top_cities[1][1].strip(), str(len(cities))),
                        '{}: {} ({}/{})'.format(top_cities[2][0].replace('\'', ''),
                                                StaticMethods.get_percentage(top_cities[2][1], str(len(cities)), 3),
                                                top_cities[2][1].strip(), str(len(cities)))))
                elif i == 2:
                    repl.append('\n\nUniversity:\n{}\n{}\n{}'.format(
                        '{}: {} ({}/{})'.format(top_cities[0][0].replace('\'', ''),
                                                StaticMethods.get_percentage(top_cities[0][1], str(len(cities)), 3),
                                                top_cities[0][1].strip(), str(len(cities))),
                        '{}: {} ({}/{})'.format(top_cities[1][0].replace('\'', ''),
                                                StaticMethods.get_percentage(top_cities[1][1], str(len(cities)), 3),
                                                top_cities[1][1].strip(), str(len(cities))),
                        '{}: {} ({}/{})'.format(top_cities[2][0].replace('\'', ''),
                                                StaticMethods.get_percentage(top_cities[2][1], str(len(cities)), 3),
                                                top_cities[2][1].strip(), str(len(cities)))))
                    self.save(repl)
                    if not Config.module_mod:
                        StaticData.log.log(text=' '.join(repl), type_s='success_w')
                    StaticData.log.log(text='\n', type_s='print')
                    StaticData.log.log(text='User with ID {} handled.'.format(self.user_id), type_s='success')
            except:
                pass
