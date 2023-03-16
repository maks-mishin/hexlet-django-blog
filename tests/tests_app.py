from django.test import TestCase
from hexlet_django_blog.factories import CategoryFactory


class CategoriesTest(TestCase):

    def setUp(self):
        self.category1 = CategoryFactory()
        self.category2 = CategoryFactory()

    def test_category_view(self):
        response = self.client.get('/categories/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.category1.name)
        self.assertContains(response, self.category2.name)

    def test_category_delete(self):
        response = self.client.post(f'/categories/{self.category1.id}/delete/')
        self.assertEqual(response.status_code, 302)
        response = self.client.get('/categories/')
        self.assertNotContains(response, self.category1.name)
        self.assertContains(response, self.category2.name)
