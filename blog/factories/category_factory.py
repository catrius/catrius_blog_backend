from factory import DjangoModelFactory, Faker


class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = 'blog.Category'

    name = Faker('word')
    description = Faker('sentence')
