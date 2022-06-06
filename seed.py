import random as rd
from faker import Faker

from api import create_app
from api.database import db
from api.user.models import User
from api.transaction.models import Account

USER_COUNT = 50
ACCOUNT_COUNT = 100
ACCOUNT_TYPES = ['Crypto', 'Stocks', 'Bank', 'Credit']


def truncate_tables():
    """Delete all rows from database tables"""
    Account.query.delete()
    User.query.delete()
    db.session.commit()


def get_random_user_id():
    users = User.get_all()
    rand_user = users[rd.randint(0, len(users) - 1)]
    return rand_user.id


def main():
    app = create_app()
    app.app_context().push()
    truncate_tables()
    fake = Faker()


    # Generate users
    for _ in range(USER_COUNT):
        rand_user = {
            'username': fake.unique.first_name().lower() + str(rd.randint(1, 150)),
            'email': fake.unique.email(),
            'password': fake.password(length=256)
        }
        User.create(**rand_user)


    for _ in range(ACCOUNT_COUNT):
        rand_account = {
            'name': fake.company(),
            'type': ACCOUNT_TYPES[rd.randint(0, len(ACCOUNT_TYPES) - 1)],
            'user_id': get_random_user_id()
        }
        Account.create(**rand_account)



if __name__ == '__main__':
    main()