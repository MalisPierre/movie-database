from django.db import models
from datetime import datetime
from multiselectfield import MultiSelectField

class MovieGenre(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Titre", help_text="Le titre du genre", blank=False, null=False)
    remote_id = models.IntegerField(default=0)

    def __str__(self):
        return self.name



# class MovieGenre(models.TextChoices):
#     HORROR = "horror", "Horreur"
#     WESTERN = 'western', "Western"
#     MAFIA = 'mafia', "Mafia"
#     FANTASY = 'fantasy', 'Fantastique'
#     SCIENCE_FICTION = 'sci-fi', 'Science Fiction'
#     HISTORIC = "historic", "Historique"
#     CARTOON = "cartoon", "Dessin Animé"
#     COMEDY = "comedy", "Comédie"

class MovieStatus(models.TextChoices):
    DEV = "in_development", "En développement"
    PROD = "in_production", "En production"
    PUBLISH = 'published', "publié"
    CANCEL = 'cancelled', "annulé"

class Movie(models.Model):

    title = models.CharField(
        max_length=100,
        verbose_name="Titre", help_text="Le titre du film", blank=False, null=False)
    homepage = models.TextField(
        max_length=2048,
        verbose_name="Homepage", help_text="Le contenu de la page du film", blank=False, null=False)
    release_date = models.DateField(
        verbose_name="Date de sortie", help_text="La date de parution du film",
        default=None, blank=False, null=False)

    adult = models.BooleanField(verbose_name="Pour adulte", help_text="Film réservé pour adultes",)
    budget = models.IntegerField(
        verbose_name="Budget", help_text="Le budget du film",
        default=0, null=False)
    # genre = MultiSelectField(
    #     choices=MovieGenre,
    #     verbose_name="Genres", help_text="Les genres du film")
    genre = models.ManyToManyField(MovieGenre,
        verbose_name="Genres", help_text="Les genres du film")
    status = models.TextField(
        choices=MovieStatus, max_length=64,
        verbose_name="Statut", help_text="Le statut du film", blank=False, null=False, default=MovieStatus.DEV)
    cover = models.FileField(upload_to="cover", verbose_name="Image de couverture", help_text="L'image de couverture du film'", null=True)

    def __str__(self):
        return self.title + " - " + str(self.release_date.year)

    def average_note(self):
        from spectator.models import MovieReview
        from django.db.models import Avg
        average = MovieReview.objects.filter(movie__id=self.id).aggregate(average_note=Avg("note"))
        return round(average["average_note"], 1) if average and average["average_note"] else "-"

        