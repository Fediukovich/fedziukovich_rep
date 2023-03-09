
# class_task_4

from pydantic import BaseModel


class CategoryModel(BaseModel):
    name: str
    is_published: bool = False

    class Config:
        orm_mode = True


class Category(object):

    categories: list[CategoryModel] = []

    @classmethod
    def add(cls, new_category: CategoryModel) -> int:
        # for category in cls.categories:
        #     if category.name == new_category.name:
        #         raise ValueError('new category is not unique')
        objs = [*filter(lambda x: x.name == new_category.name, cls.categories)]
        if objs:
            raise ValueError('new category is not unique')

        cls.categories.append(new_category)
        return len(cls.categories) - 1

    @classmethod
    def get(cls, id_: int) -> CategoryModel:
        # easier to ask for forgiveness than permission (eafp)
        # if 0 <= id_ < len(cls.categories):
        #     return cls.categories[id_]
        # try:
        #     return cls.categories[id_]
        # except IndexError:
        #     pass
        return cls.categories[id_]

    @classmethod
    def delete(cls, id_: int) -> None:
        try:
            del cls.categories[id_]
        except InterruptedError:
            pass

    @classmethod
    def update(cls, id_: int, new_name: str) -> None:
        try:
            obj = cls.get(id_)
        except IndexError:
            cls.add(CategoryModel(name=new_name))
        else:
            objs = [*filter(lambda x: x.name == new_name, cls.categories)]
            if objs:
                raise ValueError
            else:
                obj.name = new_name

    @classmethod
    def make_published(cls, *args: int) -> None:
        for i in args:
            obj = cls.get(i)
            obj.is_published = True

    @classmethod
    def make_unpublished(cls, *args: int) -> None:
        for i in args:
            obj = cls.get(i)
            obj.is_published = False