class Repository:
    def __init__(self):
        self.data=[]

    def save_to_db(self):
        pass

    def load_from_db(self):
        pass

    def get_data(self):
        return self.data

    def save_user(self, name):
        self.data.append(name)

