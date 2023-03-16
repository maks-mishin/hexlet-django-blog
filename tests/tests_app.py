from django.test import TestCase
from categories.models import Category
from hexlet_django_blog.factories import CategoryFactory


class CategoriesTest(TestCase):

    def setUp(self):
        self.category = CategoryFactory()

    def test_category_view_has_update_link(self):
        response = self.client.get('/categories/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, f'{self.category.id}/update/')

    def test_category_update_view(self):
        response = self.client.get(f'/categories/{self.category.id}/update/')
        self.assertEqual(response.status_code, 200)

    def test_category_update_post_with_validation_errors(self):
        params = {
            'name': 'b',
            'state': 'draft'
        }
        response = self.client.post(
            f'/categories/{self.category.id}/update/',
            data=params
        )
        self.assertIn('description', response.context['form'].errors)

        params = {
            'name': 'name' * 26,
            'description': 'lala' * 50,
            'state': 'draft'
        }
        response = self.client.post(
            f'/categories/{self.category.id}/update/',
            data=params
        )
        self.assertIn('name', response.context['form'].errors)

        params = {
            'name': 'name',
            'description': 'lala' * 50,
            'state': 'drift'
        }
        response = self.client.post(
            f'/categories/{self.category.id}/update/',
            data=params
        )
        self.assertIn('state', response.context['form'].errors)

    def test_category_update(self):
        params = {
            'name': 'a',
            'description': 'lala' * 50,
            'state': 'draft',
        }
        response = self.client.post(
            f'/categories/{self.category.id}/update/',
            data=params,
        )
        self.assertEqual(response.status_code, 302)
        updated_category = Category.objects.get(name='a')
        self.assertEqual(updated_category.name, params['name'])
