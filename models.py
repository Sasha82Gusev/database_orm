import sqlalchemy
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()


DSN = "postgresql://postgres:41321122@localhost:5432/123"
engine = sqlalchemy.create_engine(DSN)

class Publisher(Base):
    __tablename__ = "publisher"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    publisher_name = sqlalchemy.Column(sqlalchemy.String(length=100), nullable=False, unique=True)

    def __str__(self):
        return f'Publisher {self.id} : ({self.publisher_name})'



class Book(Base):
    __tablename__ = "book"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    book_title = sqlalchemy.Column(sqlalchemy.String(length=100), nullable=False)
    id_publisher = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("publisher.id"), nullable=False)
    publisher = relationship(Publisher, backref="book")

    def __str__(self):
        return f'Book {self.id} : ({self.book_title}, {self.id_publisher})'



class Shop(Base):
    __tablename__ = "shop"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    shop_name = sqlalchemy.Column(sqlalchemy.String(length=100), nullable=False)

    def __str__(self):
        return f'Shop {self.id} : ({self.shop_name})'



class Stock(Base):
    __tablename__ = "stock"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    stock_count = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    id_book = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("book.id"), nullable=False)
    id_shop = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("shop.id"), nullable=False)
    book = relationship(Book, backref="stock")
    shop = relationship(Shop, backref="stock")

    def __str__(self):
        return f'Stock {self.id} : ({self.stock_count}, {self.id_book}, {self.id_shop})'



class Sale(Base):
    __tablename__ = "sale"

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    sale_price = sqlalchemy.Column(sqlalchemy.Numeric, nullable=False)
    sale_date = sqlalchemy.Column(sqlalchemy.DateTime, nullable=False)
    sale_count = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    id_stock = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("stock.id"), nullable=False)
    stock = relationship(Stock, backref="sale")

    def __str__(self):
        return f'Sale {self.id} : ({self.sale_price}, {self.sale_date}, {self.sale_count}, {self.id_stock})'



Base.metadata.create_all(engine)

def create_tables(engine):
     Base.metadata.create_all(engine)

# def drop_tables(engine):
#     Base.metadata.drop_all(engine)