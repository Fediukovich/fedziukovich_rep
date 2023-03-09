from inspect import iscoroutinefunction

from sqlalchemy import Column, INT, VARCHAR, DECIMAL, ForeignKey, create_engine, select, desc
from sqlalchemy.orm import DeclarativeBase, declared_attr, sessionmaker, Session
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession


class Base(DeclarativeBase):
    id = Column(INT, primary_key=True)

    engine = create_engine('postgresql://dev:password@localhost:5432/bhcorp')
    async_engine = create_async_engine('postgresql+asyncpg://dev:password@localhost:5432/bhcorp')
    session = sessionmaker(bind=engine)
    async_session = async_sessionmaker(bind=async_engine)

    @declared_attr
    def __tablename__(cls) -> str:
        return ''.join(f'_{i.lower()}' if i.isupper() else i for i in cls.__name__).strip('_')

    @staticmethod
    def create_session(func):
        async def async_wrapper(*args, **kwargs):
            async with Base.async_session() as session:
                return await func(*args, **kwargs, session=session)

        def wrapper(*args, **kwargs):
            with Base.session() as session:
                return func(*args, **kwargs, session=session)

        return async_wrapper if iscoroutinefunction(func) else wrapper

    @create_session
    async def save(self, session: AsyncSession = None):
        session.add(self)
        await session.commit()
        await session.refresh(self)

    @classmethod
    @create_session
    async def get(cls, id_, session: AsyncSession = None):
        return await session.get(cls, id_)

    @create_session
    async def delete(self, session: AsyncSession = None):
        await session.delete(self)
        await session.commit()

    @classmethod
    @create_session
    async def all(
            cls,
            order_by: str = 'id',
            limit: int = None,
            offset: int = None,
            session: AsyncSession = None,
            **kwargs
    ):
        objs = await session.scalars(
            select(cls)
            .order_by(order_by)
            .limit(limit)
            .offset(offset)
            .filter_by(**kwargs)
        )
        return objs.all()

    def dict(self) -> dict:
        data = self.__dict__
        if '_sa_instance_state' in data:
            del data['_sa_instance_state']
        return data

    def __call__(
            self,
            order_by: str = 'id',
            **kwargs
    ):
        if order_by.startswith('-'):
            order_by = desc(order_by.removeprefix('-'))
        setattr(self, '__filter', kwargs)
        setattr(self, '__order_by', order_by)
        return self.__aiter__()

    def __aiter__(self):
        return self

    async def __anext__(self):
        i = getattr(self, 'i', False)
        if not i:
            setattr(self, 'i', 0)
        _filter = getattr(self, '__filter', {})
        order_by = getattr(self, '__order_by', 'id')
        async with self.async_session() as session:
            obj = await session.scalars(
                select(self.__class__)
                .order_by(order_by)
                .filter_by(**_filter)
                .limit(1)
                .offset(i)
            )
            setattr(self, 'i', i + 1)
            obj = obj.all()
            if obj:
                return obj[0]
            else:
                setattr(self, 'i', 0)
                raise StopAsyncIteration


class Category(Base):
    # __tablename__ = 'category'

    name = Column(VARCHAR(64), unique=True, nullable=False)

    def __repr__(self):
        return self.name


class Product(Base):
    # __tablename__ = 'product'

    name = Column(VARCHAR(128), nullable=False)
    price = Column(DECIMAL(6, 2), nullable=False)
    category_id = Column(ForeignKey('category.id', ondelete='CASCADE'), nullable=False)


class ProductImage(Base):
    url = Column(VARCHAR(256), nullable=False)
    product_id = Column(ForeignKey('product.id', ondelete='CASCADE'), nullable=False)


class User(Base):
    email = Column(VARCHAR(128), nullable=False, unique=True)
    hashed_password = Column(VARCHAR(512), nullable=False)