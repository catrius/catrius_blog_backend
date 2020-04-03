from factory import DjangoModelFactory, Faker, SubFactory, Sequence

from blog.factories.category_factory import CategoryFactory


class PostFactory(DjangoModelFactory):
    class Meta:
        model = 'blog.Post'

    title = Sequence(lambda n: f'Post {n}')
    category = SubFactory(CategoryFactory)
    content = Faker('text')
    excerpt = Faker('text')
    thumbnail = Sequence(lambda n: f'/media/photos/post-{n}.jpeg')
    caption = Faker('sentence')
    image_showing = Faker('pybool')
