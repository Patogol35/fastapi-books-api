from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, crud
from database import SessionLocal, engine, Base

# Crear tablas en la BD
Base.metadata.create_all(bind=engine)

app = FastAPI(title="API de Libros con FastAPI y MySQL")

# Dependencia para obtener sesión de BD
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/books", response_model=list[schemas.Book])
def read_books(db: Session = Depends(get_db)):
    return crud.get_books(db)

@app.get("/books/{book_id}", response_model=schemas.Book)
def read_book(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.get_book(db, book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return db_book

@app.post("/books", response_model=schemas.Book)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db, book)

@app.put("/books/{book_id}", response_model=schemas.Book)
def update_book(book_id: int, book: schemas.BookCreate, db: Session = Depends(get_db)):
    db_book = crud.update_book(db, book_id, book)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return db_book

@app.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    success = crud.delete_book(db, book_id)
    if not success:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return {"message": "Libro eliminado"}

