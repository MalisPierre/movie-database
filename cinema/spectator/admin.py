from django.contrib import admin
from spectator.models import Spectator, AuthorReview, MovieReview
# Register your models here.
admin.site.register(MovieReview)
admin.site.register(AuthorReview)
admin.site.register(Spectator)