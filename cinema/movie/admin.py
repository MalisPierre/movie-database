from django.contrib import admin
from movie.models import Movie, MovieStatus, MovieGenre
from django.shortcuts import redirect, render
from adminplus.sites import AdminSitePlus
from movie.utils import import_movie_genres, import_movies
from spectator.models import MovieReview, AuthorReview
from author.models import Author, AuthorToMovie
from spectator.models import Spectator
admin.site = AdminSitePlus()
admin.site.register(Movie)
admin.site.register(MovieGenre)

def clear_database(request, *args, **kwargs):
    movies = Movie.objects.all()
    for movie in movies:
        movie.delete()

    genres = MovieGenre.objects.all()
    for genre in genres:
        genre.delete()

    movie_reviews = MovieReview.objects.all()
    for movie in movie_reviews:
        movie.delete()

    author_reviews = AuthorReview.objects.all()
    for author in author_reviews:
        author.delete()

    roles = AuthorToMovie.objects.all()

    for role in roles:
        role.delete()
        
    authors = Author.objects.all()
    for author in authors:
        author.delete()

    specs = Spectator.objects.all()
    for spec in specs:
        spec.delete()

    return redirect('/admin')


def populate_database(request, *args, **kwargs):
    from django.core.management import call_command
    call_command('loaddata', 'fixtures/author.json', verbosity=0)
    call_command('loaddata', 'fixtures/spectator.json', verbosity=0)
    return redirect('/admin')

def import_the_movie_database(request, *args, **kwargs):
    genres = import_movie_genres()
    print(genres)
    for data in genres:
        genre = MovieGenre.objects.create(
            name = data["name"],
            remote_id = data['id']
        )
        genre.save()

# class Movie(models.Model):
    # title
    # homepage
    # release_date
    # adult 
    # budget
    # genre 
    # status 
    # cover
    movies = import_movies()
    for data in movies:
        genre_ids = data['genre_ids']
        genres = MovieGenre.objects.filter(remote_id__in=genre_ids)
        # {'adult': False, 'backdrop_path': '/zfbjgQE1uSd9wiPTX4VzsLi0rGG.jpg', 'genre_ids': [18, 80], 'id': 278, 'original_language': 'en', 'original_title': 'The Shawshank Redemption', 'overview': 'Imprisoned in the 1940s for the double murder of his wife and her lover, upstanding banker Andy Dufresne begins a new life at the Shawshank prison, where he puts his accounting skills to work for an amoral warden. During his long stretch in prison, Dufresne comes to be admired by the other inmates -- including an older prisoner named Red -- for his integrity and unquenchable sense of hope.', 'popularity': 29.9461, 'poster_path': '/9cqNxx0GxF0bflZmeSMuL5tnGzr.jpg', 'release_date': '1994-09-23', 'title': 'The Shawshank Redemption', 'video': False, 'vote_average': 8.712, 'vote_count': 28467}
        movie = Movie.objects.create(
            title=data['title'],
            homepage=data['overview'],
            release_date=data["release_date"],
            adult=data["adult"],
            budget=1,
            status=MovieStatus.PUBLISH,
            cover=None,
        )
        movie.genre.set(genres)
        movie.save()    
    return redirect('/admin')

def test_stuff(request, *args, **kwargs):
    import requests

    url = "https://api.themoviedb.org/3/review/review_id"

    headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjN2ViNDBkNmE3ZDI4ODM5NTliZjBlZWY5YjU2YjRjMyIsIm5iZiI6MTc1MDg4NjE5MS43NTAwMDAyLCJzdWIiOiI2ODVjNjcyZmVlZDUzYmNlYzI3NGY3ZTYiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0._qggDrhzjpe3cLV1bF_EijNxZxj7AbPwmqUXQ4J-420"
    }

    response = requests.get(url, headers=headers)

    print(response.text)

admin.site.register_view('clear_database', view=clear_database, name='clear database')
admin.site.register_view('populate_database', view=populate_database, name='import database from local fixtures files')
admin.site.register_view('import_database', view=import_the_movie_database, name='import database from ze movie database')
admin.site.register_view('test', view=test_stuff, name='test_stuff - do not click')