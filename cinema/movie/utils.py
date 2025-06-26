import requests
import json

def import_movie_genres():
    url = "https://api.themoviedb.org/3/genre/movie/list?language=en"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjN2ViNDBkNmE3ZDI4ODM5NTliZjBlZWY5YjU2YjRjMyIsIm5iZiI6MTc1MDg4NjE5MS43NTAwMDAyLCJzdWIiOiI2ODVjNjcyZmVlZDUzYmNlYzI3NGY3ZTYiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0._qggDrhzjpe3cLV1bF_EijNxZxj7AbPwmqUXQ4J-420"
    }

    response = requests.get(url, headers=headers)

    datas = json.loads(response.text)['genres']
    return datas

def import_movies():
    url = "https://api.themoviedb.org/3/movie/top_rated?language=en-US&page=1"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjN2ViNDBkNmE3ZDI4ODM5NTliZjBlZWY5YjU2YjRjMyIsIm5iZiI6MTc1MDg4NjE5MS43NTAwMDAyLCJzdWIiOiI2ODVjNjcyZmVlZDUzYmNlYzI3NGY3ZTYiLCJzY29wZXMiOlsiYXBpX3JlYWQiXSwidmVyc2lvbiI6MX0._qggDrhzjpe3cLV1bF_EijNxZxj7AbPwmqUXQ4J-420"
    }

    response = requests.get(url, headers=headers)

    datas = json.loads(response.text)['results']
    return datas