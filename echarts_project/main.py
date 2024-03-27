# main.py
from db import execute_query
from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/test/db_version")
def get_db_version():
    sql = "SELECT VERSION()"
    result = execute_query(sql)
    if result:
        return {"database_version": result[0]["VERSION()"]}
    raise HTTPException(status_code=500, detail="Database connection failed.")


@app.get("/api/films/all/average_rating")
def get_all_films_average_rating() -> dict:
    sql = """
    SELECT AVG(ratings.rating) AS average_rating
    FROM films
    INNER JOIN ratings ON films.film_id = ratings.film_id;
    """
    result = execute_query(sql)
    if result:
        return {"all_films_average_rating": result}
    raise HTTPException(status_code=500, detail="Database connection failed.")


@app.get("/api/films/{film_id}/average_rating")
def get_film_average_rating(film_id: int) -> dict:
    sql = """
    SELECT AVG(r.rating) as average_rating
    FROM review r
    WHERE r.film_id = {fid}
    """.format(fid=film_id)
    result = execute_query(sql)
    if result:
        return {"film_average_rating": result}
    raise HTTPException(status_code=500, detail="Database connection failed.")


@app.get("/api/users/all/average_rating")
def get_all_users_average_rating() -> dict:
    sql = """
    SELECT AVG(ratings.rating) AS average_rating
    FROM users
    INNER JOIN ratings ON users.user_id = ratings.user_id;    
    """
    result = execute_query(sql)
    if result:
        return {"all_users_average_rating": result}
    raise HTTPException(status_code=500, detail="Database connection failed.")


@app.get("/api/users/{user_id}/average_rating")
def get_user_average_rating(user_id: int) -> dict:
    sql = """
    SELECT AVG(r.rating) as average_rating
    FROM review r
    WHERE r.customer_id = {uid}
    """.format(uid=user_id)
    result = execute_query(sql)
    if result:
        return {"user_average_rating": result}
    raise HTTPException(status_code=500, detail="Database connection failed.")


@app.get("/api/genres/all/average_rating")
def get_all_genres_average_rating():
    sql = """
    SELECT c.name as genre, AVG(f.rating) as average_rating
    FROM film f
    JOIN film_category fc ON f.film_id = fc.film_id
    JOIN category c ON fc.category_id = c.category_id
    GROUP BY c.name
    """
    result = execute_query(sql)
    if result:
        return {"all_genres_average_rating": result}
    raise HTTPException(status_code=500, detail="Database connection failed.")


@app.get("/api/genres/{genre}/average_rating")
def get_genre_average_rating(genre: str):
    sql = """
    SELECT AVG(f.rating) as average_rating 
    FROM film f 
    WHERE f.film_id IN (
        SELECT fc.film_id
        FROM film_category fc
        WHERE fc.category_id = (
            SELECT c.category_id
            FROM category c
            WHERE c.name = '{genre}'
        )
    )
    """.format(genre=genre)
    result = execute_query(sql)
    if result:
        return {"genre_average_rating": result}
    raise HTTPException(status_code=500, detail="Database connection failed.")


@app.get("/api/users/all/total_rental_days")
def get_all_users_total_rental_days():
    sql = """
    SELECT c.customer_id, SUM(DATEDIFF(r.return_date, r.rental_date)) as total_rental_days
    FROM customer c
    LEFT JOIN rental r ON c.customer_id = r.customer_id
    GROUP BY c.customer_id
    """
    result = execute_query(sql)
    if result:
        return {"all_users_total_rental_days": result}
    raise HTTPException(status_code=500, detail="Database connection failed.")


@app.get("/api/users/{user_id}/total_rental_days")
def get_user_total_rental_days(user_id: int):
    sql = """
    SELECT SUM(DATEDIFF(r.return_date, r.rental_date)) as total_rental_days
    FROM rental r
    WHERE r.customer_id = {uid}
    """.format(uid=user_id)
    result = execute_query(sql)
    if result:
        return {"user_total_rental_days": result}
    raise HTTPException(status_code=500, detail="Database connection failed.")


@app.get("/api/genres/all/total_inventory")
def get_all_genres_total_inventory() -> dict:
    sql = """
    SELECT c.name AS category_name, COUNT(i.film_id) AS total_inventory
    FROM film f
    INNER JOIN film_category fc ON f.film_id = fc.film_id
    INNER JOIN category c ON fc.category_id = c.category_id
    INNER JOIN inventory i ON f.film_id = i.film_id
    GROUP BY c.name
    ORDER BY total_inventory DESC;
    """
    result = execute_query(sql)
    if result:
        return {"all_genres_total_inventory": result}
    raise HTTPException(status_code=500, detail="Database connection failed.")


@app.get("/api/sakila-data")
def get_sakila_data():
    sample_data = {
        "labels": ["A", "B", "C", "D", "E"],
        "values": [10, 20, 15, 30, 25],
    }
    return sample_data
