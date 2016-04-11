from django.test import TestCase

from .models import Post


class DummyTestCase(TestCase):

    def test_load_posts(self):
        Post.objects.create(title='test', body='lorem ipsum')
        self.assertEqual(Post.objects.count(), 1)
