from django.test import TestCase

ARTICLE = {'id': 13, 'title': 'Be or Not to Be', 'author': 'Hamlet'}
TEXT_404 = '<a href="/">Home</a>'


class AppTest(TestCase):
    def test_article_view(self):
        self.client.post('/articles/', data=ARTICLE)
        response = self.client.get('/articles/13/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'articles/article.html')
        response = self.client.post('/articles/13/')
        self.assertEqual(response.status_code, 405)

    def test_404(self):
        response = self.client.get('/articles/404/')
        self.assertEqual(response.status_code, 404)
        self.assertContains(response, TEXT_404, status_code=404)
