import vk_api
import time
import operator
import hues

from collections import Counter
from source.StaticMethods import StaticMethods
from Config import Config


class ApiWorker:

    def __init__(self, token, user_id):
        self.token = token
        self.user_id = user_id
        self.session = None

    def get_session(self):
        try:
            self.session = vk_api.VkApi(token=self.token)
        except:
            hues.error('Bad Access Token.')
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
        f = open('./{}.txt'.format(self.user_id), 'a')
        f.write(data)
        f.close()

    def get_info(self):
        cities = []
        schools = []
        univers = []
        counter = 0
        users = self.get_friends()
        hues.success()
        for user in users:
            user_info = self.session.method('users.get', {'user_ids': user, 'fields': 'city,schools,education'})
            time.sleep(0.4)
            counter += 1
            hues.log('Users handled {}/{}'.format(str(counter), str(len(users))))
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
            print('\n\n\n')
            try:
                if i == 0:
                    out = 'City:\n{}\n{}\n{}'.format(
                        '{}: {} ({}/{})'.format(top_cities[0][0].replace('\'', ''),
                                                StaticMethods.get_percentage(top_cities[0][1], str(len(cities))),
                                                top_cities[0][1].strip(), str(len(cities))),
                        '{}: {} ({}/{})'.format(top_cities[1][0].replace('\'', ''),
                                                StaticMethods.get_percentage(top_cities[1][1], str(len(cities))),
                                                top_cities[1][1].strip(), str(len(cities))),
                        '{}: {} ({}/{})'.format(top_cities[2][0].replace('\'', ''),
                                                StaticMethods.get_percentage(top_cities[2][1], str(len(cities))),
                                                top_cities[2][1].strip(), str(len(cities))))
                    print(out)
                    self.save(out)
                elif i == 1:
                    out = '\n\nSchool:\n{}\n{}\n{}'.format(
                        '{}: {} ({}/{})'.format(top_cities[0][0].replace('\'', ''),
                                                StaticMethods.get_percentage(top_cities[0][1], str(len(cities))),
                                                top_cities[0][1].strip(), str(len(cities))),
                        '{}: {} ({}/{})'.format(top_cities[1][0].replace('\'', ''),
                                                StaticMethods.get_percentage(top_cities[1][1], str(len(cities))),
                                                top_cities[1][1].strip(), str(len(cities))),
                        '{}: {} ({}/{})'.format(top_cities[2][0].replace('\'', ''),
                                                StaticMethods.get_percentage(top_cities[2][1], str(len(cities))),
                                                top_cities[2][1].strip(), str(len(cities))))
                    print(out)
                    self.save(out)
                elif i == 2:
                    out = '\n\nUniversity:\n{}\n{}\n{}'.format(
                        '{}: {} ({}/{})'.format(top_cities[0][0].replace('\'', ''),
                                                StaticMethods.get_percentage(top_cities[0][1], str(len(cities))),
                                                top_cities[0][1].strip(), str(len(cities))),
                        '{}: {} ({}/{})'.format(top_cities[1][0].replace('\'', ''),
                                                StaticMethods.get_percentage(top_cities[1][1], str(len(cities))),
                                                top_cities[1][1].strip(), str(len(cities))),
                        '{}: {} ({}/{})'.format(top_cities[2][0].replace('\'', ''),
                                                StaticMethods.get_percentage(top_cities[2][1], str(len(cities))),
                                                top_cities[2][1].strip(), str(len(cities))))
                    print(out)
                    self.save(out)
                    print('\n')
            except:
                pass
