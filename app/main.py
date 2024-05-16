from fastapi import FastAPI
from app.database.connection import get_db
from app.models.movie import Movie
from app.schemas.movie import MovieCreate, MovieUpdate

app = FastAPI()

@app.get("/movies")
def get_movies():
    db = get_db()
    movies = db.query(Movie).all()
    return movies

@app.get("/movies/{movie_id}")
def get_movie(movie_id: int):
    db = get_db()
    movie = db.query(Movie).get(movie_id)
    return movie

@app.post("/movies")
def create_movie(movie: MovieCreate):
    db = get_db()
    new_movie = Movie(name=movie.name, year=movie.year, actors=movie.actors)
    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)
    return new_movie

@app.put("/movies/{movie_id}")
def update_movie(movie_id: int, movie: MovieUpdate):
    db = get_db()
    db.query(Movie).filter(Movie.id == movie_id).update(movie.dict(exclude_unset=True))
    db.commit()
    updated_movie = db.query(Movie).get(movie_id)
    return updated_movie

@app.delete("/movies/{movie_id}")
def delete_movie(movie_id: int):
    db = get_db()
    db.query(Movie).filter(Movie.id == movie_id).delete()
    db.commit()
    return {"message": "Movie deleted successfully"}