from django.core.management import BaseCommand
from users.models import User
from blog.models import Blog
from comments.models import Comment


class Command(BaseCommand):

    def handle(self, *args, **options):

        users = [
            {'email': '1234@yandex.ru', 'username': 'Федя', 'date_of_birth': '1999-02-01'},
            {'email': '3214@yandex.ru', 'username': 'Толя', 'date_of_birth': '2015-02-01'},
        ]

        users_list = []
        for item in users:
            users_list.append(User(**item))

        User.objects.bulk_create(users_list)

        # blog = [
        #     {'title': 'Статья1', 'user': User.objects.get(pk=3)},
        #     {'title': 'Статья2', 'user': User.objects.get(pk=3)},
        #     {'title': 'Статья3', 'user': User.objects.get(pk=3)},
        #     {'title': 'Статья4', 'user': User.objects.get(pk=4)},
        #     {'title': 'Статья5', 'user': User.objects.get(pk=4)},
        # ]
        #
        # blog_list = []
        # for item in blog:
        #     blog_list.append(Blog(**item))
        #
        # Blog.objects.bulk_create(blog_list)
        #
        # comment = [
        #     {'context': 'Хорошо', 'user': User.objects.get(pk=3), 'blog': Blog.objects.get(pk=1)},
        #     {'context': 'Плохо', 'user': User.objects.get(pk=3), 'blog': Blog.objects.get(pk=1)},
        #     {'context': 'Красито', 'user': User.objects.get(pk=3), 'blog': Blog.objects.get(pk=1)},
        #     {'context': 'Ужасно', 'user': User.objects.get(pk=4), 'blog': Blog.objects.get(pk=2)},
        #     {'context': 'Нормально', 'user': User.objects.get(pk=4), 'blog': Blog.objects.get(pk=2)},
        # ]
        #
        # comment_list = []
        # for item in comment:
        #     comment_list.append(Comment(**item))
        #
        # Comment.objects.bulk_create(comment_list)