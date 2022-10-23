import sqlalchemy
from sqlalchemy.orm import declarative_base, sessionmaker
from models import Publisher, Book, Shop, Stock, Sale


Base = declarative_base()

DSN = "postgresql://postgres:xxxxxxxx@localhost:5432/123"
engine = sqlalchemy.create_engine(DSN)

Session = sessionmaker(bind=engine)
session = Session()


def searching_publisher(action, query_publisher):
    query_join = session.query(Shop.shop_name, Publisher.id, Publisher.publisher_name).join(Stock).join(Book).join(Publisher).group_by(Shop.shop_name, Publisher.id, Publisher.publisher_name)
    if action == 1:
        query_result = query_join.filter(Publisher.id == query_publisher)
    if action == 2:
        query_result = query_join.filter(Publisher.publisher_name == query_publisher)
    for result in query_result.all():
        print("Издатель", result.publisher_name, "c ID", result.id, "найден в магазине ", result.shop_name)


if __name__ == '__main__':
    action = int(input("По какому параметру будем искать? 1-ID, 2-Имя издателя. "))
    if action == 1:
        searching_publisher(1, query_publisher=input('Введите ID (id) издателя: '))

    if action == 2:
        searching_publisher(2, query_publisher=input('Введите имя (publisher_name) издателя: '))
    session.close()
