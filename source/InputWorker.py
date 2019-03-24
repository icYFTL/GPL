class InputWorker(object):
    def get_token():
        try:
            f = open('data.txt', 'r')
            token = f.read()
            f.close()
        except:
            token = input('Vk Access Token: ')
            while True:
                if len(token) != 85:
                    token = input('[Bad Access Token] Vk Access Token: ')
                else:
                    break
            f = open('data.txt', 'w')
            f.write(token)
            f.close()
        return token

    def get_user_id():
        return input('Give me the user ID: ')
