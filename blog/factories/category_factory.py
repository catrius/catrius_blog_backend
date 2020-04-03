from factory import DjangoModelFactory, Faker, Sequence


class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = 'blog.Category'

    name = Sequence(lambda n: f'Category {n}')
    description = Faker('sentence')
