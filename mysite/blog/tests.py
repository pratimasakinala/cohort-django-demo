from django.test import client, TestCase
from django.urls import reverse

from .models import Post

# Create your tests here.
class PostTest(TestCase):
    fixtures = ['fixtures.json']

    def setUp(self):
        self.client = client.Client()

    def test_post_list(self):
        url = reverse('blog:post-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_post_detail(self):
        # debugger below
        # import code
        # code.interact(local=locals())

        post = Post.objects.filter(status= 'P').first()
        response = self.client.get(post.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertIn(post.title, response.content.decode('utf-8'))
