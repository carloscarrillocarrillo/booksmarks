from Security.db.user.CreateUserInterface import CreateUserInterface

def create_user(create_user: CreateUserInterface  ,username, password, confirm_password):
  return create_user.create(username, password, confirm_password)