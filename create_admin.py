from getpass import getpass
import sys

from webapp import create_app
from webapp.model import User, db


app = create_app()

with app.app_context():
    user_name = input('Enter username: ')

    if User.query.filter(User.user_name == user_name).count():
        print('This user name already exists')
        sys.exit(0)

    password = getpass('Enter password: ')
    password2 = getpass('Reenter password: ')
    if not password == password2:
        sys.exit(0)

    new_user = User(user_name=user_name, role='admin')
    new_user.set_password(password)

    db.session.add(new_user)
    db.session.commit()
    print('User with id {} added'.format(new_user.id))

