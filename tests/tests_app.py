from django.test import TestCase
from categories.models import Category


class CategoriesTest(TestCase):

    def test_category_view_has_create_link(self):
        response = self.client.get('/categories/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '/categories/create/')

    def test_category_create_view(self):
        response = self.client.get('/categories/create/')
        self.assertEqual(response.status_code, 200)

    def test_category_create_post_with_validation_errors(self):
        params = {
            'name': 'b',
            'state': 'draft'
        }
        response = self.client.post('/categories/create/', data=params)
        self.assertIn('description', response.context['form'].errors)

        params = {
            'name': 'name' * 26,
            'description': 'lala' * 50,
            'state': 'draft'
        }
        response = self.client.post('/categories/create/', data=params)
        self.assertIn('name', response.context['form'].errors)

        params = {
            'name': 'name',
            'description': 'lala' * 50,
            'state': 'drift'
        }
        response = self.client.post('/categories/create/', data=params)
        self.assertIn('state', response.context['form'].errors)

    def test_category_create(self):
        params = {
            'name': 'a',
            'description': 'lala' * 50,
            'state': 'draft',
        }
        response = self.client.post(
            '/categories/create/',
            data=params,
        )
        self.assertEqual(response.status_code, 302)
        created_category = Category.objects.get(name='a')
        self.assertEqual(created_category.name, params['name'])
