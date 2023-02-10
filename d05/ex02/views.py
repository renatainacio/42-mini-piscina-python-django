from django.http import HttpResponse
from django.template import loader
import psycopg2

def init(request):
    try:
        conn = psycopg2.connect(
        database = 'djangotraining',
        host = 'localhost',
        user = 'djangouser',
        password = 'secret'
        )

        curr = conn.cursor()

        curr.execute(''' CREATE TABLE IF NOT EXISTS ex02_movies (
            title varchar(64) UNIQUE NOT NULL,
            episode_nb int PRIMARY KEY,
            opening_crawl text,
            director varchar(32) NOT NULL,
            producer varchar(128) NOT NULL,
            release_date date NOT NULL
            )
            ''')

        conn.commit()
        conn.close()
        return HttpResponse("OK")
    except Exception as e:
        return HttpResponse(e)

def populate(request):
    try:
        conn = psycopg2.connect(
        database = 'djangotraining',
        host = 'localhost',
        user = 'djangouser',
        password = 'secret'
        )

        curr = conn.cursor()

        movies = [
            {
                "episode_nb": 1,
                "title": "The Phantom Menace"
                "director": "George Lucas"
                "producer": "Rick McCallum"
                "release_date": "1999-05-19"
            }
            {
                "episode_nb": 2,
                "title": "Attack of the Clones"
                "director": "George Lucas"
                "producer": "Rick McCallum"
                "release_date": "2002-05-16"
            }
            {
                "episode_nb": 3,
                "title": "Revenge of the Sith"
                "director": "George Lucas"
                "producer": "Rick McCallum"
                "release_date": "2005-05-19"
            }
            {
                "episode_nb": 4,
                "title": "A New Hope"
                "director": "George Lucas"
                "producer": "Gary Kurtz, Rick McCallum"
                "release_date": "1977-05-25"
            }
            {
                "episode_nb": 5,
                "title": "The Empire Strikes Back"
                "director": "Irvin Kershner"
                "producer": "Gary Kurtz, Rick McCallum"
                "release_date": "1980-05-17"
            }
            {
                "episode_nb": 6,
                "title": "Return of the Jedi"
                "director": "Richard Marquand"
                "producer": "Howard G. Kazanjian, George Lucas, Rick McCallum"
                "release_date": "1983-05-25"
            }
            {
                "episode_nb": 7,
                "title": "The Force Awakens"
                "director": "J. J. Abrams"
                "producer": "Kathleen Kennedy, J. J. Abrams, Bryan Burk"
                "release_date": " 2015-12-11"
            }                     
        ]


# to be fixed:

    # for movie in movies:
    #     INSERT_DATA='''INSERT INTO ex02_movies(episode_nb, title, director, producer, release_date)
    #         VALUES({episode_nb} {title} {director} {producer} {release_date});'''.format(movie[episode_nb])

    # curr.execute(INSERT_DATA)

    #     return HttpResponse("OK")
    # except Exception as e:
    #     return HttpResponse(e)