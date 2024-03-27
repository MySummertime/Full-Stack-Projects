# main.py
from fastapi import FastAPI

from db import execute_query

app = FastAPI()


@app.get("/db_version")
def get_db_version():
    sql = "SELECT VERSION()"
    result = execute_query(sql)
    if result:
        return {"database_version": result[0]["VERSION()"]}
    else:
        return {"error": "Database connection failed"}


@app.get("/employees")
def get_employees():
    sql = "SELECT * FROM EMPLOYEE"
    result = execute_query(sql)
    if result:
        return {"employees": result}
    else:
        return {"error": "Database connection failed"}


@app.get("/api/sakila-data")
def get_sakila_data():
    sample_data = {
        "labels": ["A", "B", "C", "D", "E"],
        "values": [10, 20, 15, 30, 25],
    }
    return sample_data