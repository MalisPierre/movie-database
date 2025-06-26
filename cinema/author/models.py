from django.db import models
from movie.models import Movie
from user.models import CustomUser


class Author(CustomUser):


    birthday = models.DateField(
        verbose_name="Date de naissance", help_text="La date de naissance",
        default=None, blank=False, null=False)

    def __str__(self):
        return self.first_name + " " + self.last_name
    
    def average_note(self):
        from spectator.models import AuthorReview
        from django.db.models import Avg
        average = AuthorReview.objects.filter(author__id=self.id).aggregate(average_note=Avg("note"))
        return round(average["average_note"], 1) if average and average["average_note"] else "-"
    
    def movies(self):
        movies = AuthorToMovie.objects.filter(author__id=self.id).values("id", "author__id", "movie__id", "role")
        return movies
    
    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
    



# ------------------------------------------ 


class AuthorRole(models.TextChoices):
    AUTHOR = "author", "Auteur"
    LEAD = "lead", "Acteur principal"
    SUPPORT = "support", "Acteur secondaire"


class AuthorToMovie(models.Model):
    author = models.ForeignKey(Author, 
        null=False, 
        verbose_name="Auteur / Acteur", help_text="Auteur / Acteur du film",
        related_name='authors',
        on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, 
        null=False, 
        verbose_name="Film", help_text="Film",
        related_name='movies',
        on_delete=models.CASCADE)
    role = models.CharField(
        default=AuthorRole.AUTHOR,
        verbose_name="Role", help_text="Role dans le film", 
        choices=AuthorRole)


    def __str__(self):
        return str(self.author) + " " + str(self.movie)