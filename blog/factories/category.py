import factory


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'blog.Category'

    name = factory.Faker('word')
    description = factory.Faker('sentence')
