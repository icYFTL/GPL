import vk_api
import time

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
        city_count = Counter(cities)
        schools_count = Counter(schools)
        univers_count = Counter(univers)

        return [city_count, schools_count, univers_count]
