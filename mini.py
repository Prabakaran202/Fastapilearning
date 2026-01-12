from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# 1. Pydantic Model (பெயர்களைச் சரி செய்துள்ளேன்)
class Movie(BaseModel):
    name: str
    year: int
    rating: float  # reding -> rating
    director: str  # dreater -> director

class MovieResponse(BaseModel):
    msg: str
    movie: Optional[Movie] = None # மூவி இல்லைனா Error வராம இருக்க Optional

# Mock Database
db = [
    {"name": "Prabs", "year": 2000, "rating": 4.1, "director": "Avan"},
    {"name": "Nee", "year": 3000, "rating": 9.1, "director": "Suratha"},
    {"name": "Kathir", "year": 2000, "rating": 8.2, "director": "Kumar"}
]

# Task 2: POST Method - புது மூவி சேர்க்க
@app.post("/movie_list/", response_model=MovieResponse)
async def create_movie(new_movie: Movie):
    db.append(new_movie.model_dump()) # Pydantic v2-வில் .dict() க்கு பதில் .model_dump()
    return {"msg": "New movie added successfully", "movie": new_movie}

# Task 3: Path Parameter - ID வைத்து எடுக்க
@app.get("/movie_list/{movie_id}", response_model=MovieResponse)
async def get_movie_by_id(movie_id: int):
    if movie_id < 0 or movie_id >= len(db):
        # 404 Error காட்டுவதுதான் சரியான முறை
        raise HTTPException(status_code=404, detail="Movie not found")
    
    return {"msg": "Your movie found", "movie": db[movie_id]}

# Task 4: Query Parameter - வருஷத்தை வைத்து Filter செய்ய (இந்த வாரம் இதுதான் புதுசு!)
@app.get("/movies/filter/")
async def filter_movies(year: Optional[int] = None):
    if year:
        # வருஷம் மேட்ச் ஆகுற மூவிகளை மட்டும் எடுக்கும் logic
        results = [m for m in db if m["year"] == year]
        return {"year_filtered": year, "results": results}
    return {"msg": "No year provided", "all_movies": db}