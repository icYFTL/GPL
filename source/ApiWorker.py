import vk_api
import time
import operator

from collections import Counter


class ApiWorker:

    def __init__(self, token, user_id):
        self.token = token
        self.user_id = user_id
        self.session = ""

    def get_session(self):
        try:
            self.session = vk_api.VkApi(token=self.token)
        except:
            print('Bad Access Token.')
            exit()

    def get_friends(self):
        self.get_session()
        try:
            return self.session.method('friends.get', {'user_id': self.user_id}).get('items')
        except:
            return False

    def get_info(self):
        cities = []
        schools = []
        univers = []
        users = self.get_friends()
        for user in users:
            user_info = self.session.method('users.get', {'user_ids': user, 'fields': 'city,schools,education'})
            time.sleep(0.4)
            print(user_info)
            try:
                cities.append(user_info[0].get('city').get('title'))
            except:
                pass
            try:
                schools.append(user_info[0].get('schools')[-1].get('name'))
            except:
                pass
            try:
                univer = user_info[0].get('university_name')
                if univer != None and univer != '':
                    univers.append(univer)
            except:
                pass
        data = [Counter(cities), Counter(schools), Counter(univers)]
        top_cities = [None] * 3
        for i in range(len(data)):
            if len(data[0]) > 2:
                top_cities[0] = str(sorted(dict(data[i]).items(), key=operator.itemgetter(1))[-1]).replace('(', '').replace(')', '').split(',')
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
            if i == 0:
                print('City:\n{} or {} or {}'.format(top_cities[0], top_cities[1], top_cities[2]))
            elif i == 1:
                print('School:\n{} or {} or {}'.format(top_cities[0], top_cities[1], top_cities[2]))
            elif i == 2:
                print('University:\n{} or {} or {}'.format(top_cities[0], top_cities[1], top_cities[2]))
