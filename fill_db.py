from database_setup import User, Base, Item, Category
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


engine = create_engine('sqlite:///itemcatalog.db',
                       connect_args={'check_same_thread': False})


Session = sessionmaker(bind=engine)


session = Session()

pic = 'https://bit.ly/30W7hoC'
user1 = User(
    name='mohamed',
    email='mido4@gmail.com',
    picture=pic
)
user2 = User(
    name='ahmed',
    email='ahmed32158@gmail.com',
    picture=pic
)
user3 = User(
    name='mahmoud',
    email='midomah@gmail.com',
    picture=pic
)
user4 = User(
    name='kamel',
    email='kamel32158@gmail.com',
    picture=pic
)
user5 = User(
    name='raul',
    email='raul4@gmail.com',
    picture=pic
)
user6 = User(
    name='dada',
    email='dodo32158@gmail.com',
    picture=pic
)

session.add(user1)
session.add(user2)
session.add(user3)
session.add(user4)

session.commit()

category1 = Category(
    name='Soccer',
    user=user1
)
category2 = Category(
    name='movies',
    user=user2
)
category3 = Category(
    name='series',
    user=user3
)
category4 = Category(
    name='stories',
    user=user4
)

session.add(category1)
session.add(category2)
session.add(category3)
session.add(category4)

session.commit()

item1 = Item(
    name='Barcelona',
    description='the great spanish team',
    category=category1,
    user=user1
)
item2 = Item(
    name='Egyptian national team',
    description='the greatest national team in africa',
    category=category1,
    user=user1
)
item3 = Item(
    name='titanic',
    description='a film about the great ship',
    category=category2,
    user=user2
)
item4 = Item(
    name='batman',
    description='a film about the great super hero ',
    category=category2,
    user=user2
)
item5 = Item(
    name='big bang theory',
    description='comedy one ',
    category=category3,
    user=user3
)
item6 = Item(
    name='mr robot',
    description=' a good series',
    category=category3,
    user=user3
)
item7 = Item(
    name='the old man and the sea',
    description='a story by ernest hemingway',
    category=category4,
    user=user4
)
item8 = Item(
    name='oliver twist',
    description='a story by charles dickens',
    category=category4,
    user=user4
)


session.add(item1)
session.add(item2)
session.add(item3)
session.add(item4)
session.add(item5)
session.add(item6)
session.add(item7)
session.add(item8)

session.commit()

print('Done')
