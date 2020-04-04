from factory import DjangoModelFactory, Faker, Sequence


class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = 'blog.Category'

    name = Faker('sentence')
    description = Faker('sentence')
