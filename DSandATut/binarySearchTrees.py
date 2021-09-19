#problem: build a BST that is able to insert, find, upadate and list user info of unique usernames

class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email
        print('User created!')
    
    def __repr__(self):
        return "User(username = '{}', name = '{}', email = '{}'".format(self.username, self.name, self.email)
    
    def __str__(self):
        return self.__repr__()

    def introduce(self, guest_name):
        print("hi {}, I'm {}! Contact me at {}.", format(guest_name, self.name, self.email))

user1 = User('jonsmith1', 'Jon Smith', 'js123@gmail.com')


class UserDatabase:
    def __init__(self):
        self.users = []

    def insert(self, user):
        i = 0
        while i < len(self.users):
            if self.users[i].username > user.username:
                break
            i+=1
        self.users.insert(i, user)
    def find(self, username):
        pass
    def update(self, user):
        pass
    def list_all(self):
        pass

aakash = User('aakash', 'Aakash Rai', 'aakash@example.com')
biraj = User('biraj', 'Biraj Das', 'biraj@example.com')
hemanth = User('hemanth', 'Hemanth Jain', 'hemanth@example.com')
jadhesh = User('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
siddhant = User('siddhant', 'Siddhant Sinha', 'siddhant@example.com')
sonaksh = User('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
vishal = User('vishal', 'Vishal Goel', 'vishal@example.com')

users = [aakash, biraj, hemanth, jadhesh, siddhant, sonaksh, vishal]

database = UserDatabase()
database.insert(aakash)
database.insert(jadhesh)
database.insert(biraj)

user = database.find('biraj')
print(user)
