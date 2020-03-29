from factory import DjangoModelFactory, Faker, SubFactory

from blog.factories.category_factory import CategoryFactory


class PostFactory(DjangoModelFactory):
    class Meta:
        model = 'blog.Post'

    title = Faker('sentence')
    category = SubFactory(CategoryFactory)
    content = Faker('text')
    excerpt = Faker('text')
    image_showing = False
