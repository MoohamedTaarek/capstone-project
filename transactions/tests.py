# from django.test import TestCase
# from django.contrib.auth.models import User
# from transactions.models import Post, Transaction


# class testCreate(TestCase):


#     @classmethod
#     def setUp(self):
#         test_Transaction = Transaction.objects.create(name='test')
#         test1 = User.objects.create_user(username = 'test1', password='123')

#         test_Post = Post.objects.create(
#             Transaction_id = 1,
#             title = 'test',
#             author_id = 1,
#             excerpt = 'test',
#             content = 'test')



#     def test_Transaction_content(self):
#         post = Post.postobjects.get(id=1)
#         transaction = Transaction.objects.get(id=1)
#         author = f'{post.author}'
#         excerpt = f'{post.excerpt}'
#         content = f'{post.content}'
#         status = f'{post.status}'
#         content = f'{post.content}'
#         self.assertEqual(author, 'test1')
#         self.assertEqual(excerpt, 'test')
#         self.assertEqual(content, 'test')
#         self.assertEqual(status, 'published')