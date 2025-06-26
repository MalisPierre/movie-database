from django.contrib import admin
from author.models import AuthorToMovie, Author
# Register your models here.
admin.site.register(Author)
admin.site.register(AuthorToMovie)