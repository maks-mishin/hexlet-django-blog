import factory
import factory.random
from articles.models import Article
from categories.models import Category

SEED = 4321

factory.random.reseed_random(SEED)


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker('word')
    description = factory.Faker('sentence', nb_words=4)
    state = 'published'


class ArticleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Article

    title = factory.Faker('sentence', nb_words=5)
    body = factory.Faker('paragraph', nb_sentences=5, variable_nb_sentences=False)
    category = factory.SubFactory(CategoryFactory)
