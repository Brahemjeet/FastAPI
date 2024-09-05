from fastapi import FastAPI
from typing import Any
app = FastAPI()

@app.get("/books/{book_id}")
async def read_book(book_id : int):
    return {
        "book_id" : book_id,
        "title" : "The Great Gatsby",
        "author" : "F. Scott Fitzgerald"
    }
    
@app.get("/authors/{author_id}")
async def read_author(author_id : int):
    return {
        "author_id" : author_id,
        "name" : "Ernest Hemingway"
    }
    
@app.get("/books")
async def read_books(year : int = None ):
    if year:
        return{
            "year" : year,
            "books" : ["Book1", "Book2"]
        }
    return {"books" : ["All Books"]}



from models import Book
@app.post("/book")
async def create_book(book : Book):
    return book


from pydantic import BaseModel
class BookResponse(BaseModel):
    title:str
    author: str

@app.get("allbooks", response_model=list[BookResponse])
async def read_all_books() -> Any: # async def read_all_books() -> list[BookResponse]
    return [
        {
            "id" : 1,
            "title" : "1984",
            "author": "Windy CSGO"},
        {
            "id" : 1,
            "title" : "Great Fighter",
            "author": "Sachin Tendulkar"},
    ]


from fastapi import HTTPException
from starlette.responses import JSONResponse
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message" : "Oops! Something went wrong"},
    )
    
@app.get("/error_endpoint")
async def raise_exception():
    raise HTTPException(status_code=400)



import json
from fastapi import Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return PlainTextResponse(
        "This is a plain text response:"
        f"\n{json.dumps(exc.errors(), indent=2)}", 
        status_code=status.HTTP_400_BAD_REQUEST
    )


