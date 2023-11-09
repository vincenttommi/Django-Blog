from django.apps import AppConfig
import sys
print(sys.path)


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
