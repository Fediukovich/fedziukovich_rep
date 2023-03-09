from sqlalchemy import Column, INT, VARCHAR, SMALLINT, CHAR, ForeignKey, create_engine, select
from sqlalchemy.orm import DeclarativeBase, relationship, declared_attr, sessionmaker


class Base(DeclarativeBase):
    pk = Column('id', INT, primary_key=True)

    engine = create_engine('postgresql://dev:password@localhost:5432/bpc')
    session = sessionmaker(bind=engine)

    @declared_attr
    def __tablename__(cls):
        return ''.join(f'_{i.lower()}' if i.isupper() else i for i in cls.__name__).strip('_')

    def save(self):
        with self.session() as session:
            session.add(self)
            session.commit()
            session.refresh(self)

    @classmethod
    def save_all(cls, *args):
        with cls.session() as session:
            session.add_all(args)
            session.commit()

    @classmethod
    def scalars(cls, sql):
        with cls.session() as session:
            response = session.scalars(sql)
            return response.all()


class Language(Base):
    code = Column(CHAR(2), nullable=False, unique=True)

    # users = relationship('User', back_populates='language')

    def __repr__(self):
        return self.code


class User(Base):
    email = Column(VARCHAR(128), nullable=False, unique=True)
    username = Column(VARCHAR(128), nullable=False)
    language_id = Column(SMALLINT, ForeignKey('language.id', ondelete='RESTRICT'), nullable=False)
    language = relationship('Language', backref='users')

    def __repr__(self):
        return self.email


# vasya = User(email='vasya@info.com', username='vasya', language_id=5)
# with User.session() as session:
# session.add(vasya)
# session.commit()
# session.refresh(vasya)
# print(vasya.pk)
# print(vasya.language)

# with User.session() as session:
#     # vasya = session.get(User, 1)
#     # print(vasya)
#     objs = session.execute(
#         select(User, Language)
#         .order_by(User.email)
#         .join(Language, User.language_id == Language.pk)
#     )
#     print(objs.all())
from threading import *
from queue import Queue
from time import sleep


lock = Lock()
# q = Queue()
# s = Semaphore(5)
# b = Barrier(5)
# e = Event()
# e.is_set()
# e.wait()
# q.qsize()
# q.empty()
# q.full()
# q.put()
# q.put_nowait()
# q.get()


def main():
    for i in range(10):
        lock.acquire()
        print(current_thread().name)
        lock.release()
        sleep(1)


# thread = Thread(target=main, name='CustomThread')
# thread.start()
# thread.join(timeout=5)
# thread.is_alive()