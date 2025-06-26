sudo docker-compose build


sudo docker-compose up


sudo docker-compose exec django python manage.py makemigrations

sudo docker-compose exec django python manage.py migrate

sudo docker-compose exec django python manage.py createsuperuser

http://localhost:8000/home/