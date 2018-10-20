import uuid

'''User model'''
class User(object):
   '''class to represent user model'''
   def __init__(self):
       """ Initializes empty users list"""
       self.users = []

   def add_user(self, fname, lname, username, password, role):
       """creates a new user and appends to the list"""
       if username in self.users:
            return {"message":"Username already exists, enter a different one!"}
       self.new_user = {}
       self.new_user['id'] = str(uuid.uuid4())
       self.new_user['fname'] = fname
       self.new_user['lname'] = lname
       self.new_user['username'] = username
       self.new_user['password'] = password
       self.new_user['role'] = role
       self.users[username] = self.new_user
       return {"message" : "{} added successfully".format(username)}





    