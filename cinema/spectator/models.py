from django.db import models
from user.models import CustomUser
from movie.models import Movie
from author.models import Author

class Spectator(CustomUser):

    avatar = models.FileField(upload_to="avatar", verbose_name="Avatar", help_text="L'image du profil", null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        verbose_name = 'Spectator'
        verbose_name_plural = 'Spectators'


class NoteChoice(models.IntegerChoices):
    ONE = 1, 'Un'
    TWO = 2, 'Deux'
    THREE = 3, 'Trois'
    FOUR = 4, 'Quatre'
    FIVE = 5, 'Cinq'

class AuthorReview(models.Model):
    user = models.ForeignKey(Spectator, 
        null=False, 
        verbose_name="Spectateur", help_text="Spectateur",
        on_delete=models.CASCADE)
    author = models.ForeignKey(Author, 
        null=False, 
        verbose_name="Auteur / Acteur", help_text="Auteur / Acteur",
        related_name='authorReviews',
        on_delete=models.CASCADE)
    note = models.IntegerField(
        verbose_name="Note", help_text="Note du film", 
        choices=NoteChoice)
    
    def __str__(self):
        return str(self.author) + " " + str(self.note)

class MovieReview(models.Model):
    user = models.ForeignKey(Spectator, 
        null=False, 
        verbose_name="Spectateur", help_text="Spectateur",
        on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, 
        null=False, 
        verbose_name="Film", help_text="Film",
        related_name='movieReviews',
        on_delete=models.CASCADE)
    note = models.IntegerField(
        default=NoteChoice.ONE,
        verbose_name="Note", help_text="Note du film", 
        choices=NoteChoice)
    
    def __str__(self):
        return str(self.movie) + " " + str(self.note)