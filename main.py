from typing import Annotated

from fastapi import Depends, FastAPI, Path, Query
from sqlmodel import Session, SQLModel, create_engine

from models import HeroCreate, HeroPublic, HeroUpdate
from services import hero_service

# SQLite Database
sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)


# Create database tables
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


# Database session dependency
def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]

app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


# Create Hero
@app.post("/heroes/", response_model=HeroPublic)
def create_hero(hero: HeroCreate, session: SessionDep):
    return hero_service.create_hero(session, hero)


# Get All Heroes
@app.get("/heroes/", response_model=list[HeroPublic])
def read_heroes(
    session: SessionDep,
    offset: int = Query(default=0, ge=0),
    limit: int = Query(default=100, ge=1, le=100),
):
    return hero_service.read_heroes(
        session=session,
        offset=offset,
        limit=limit,
    )


# Get Hero by ID
@app.get("/heroes/{hero_id}", response_model=HeroPublic)
def read_hero(
    hero_id: Annotated[int, Path(gt=0)],
    session: SessionDep,
):
    return hero_service.read_hero(
        session=session,
        hero_id=hero_id,
    )


# Update Hero
@app.patch("/heroes/{hero_id}", response_model=HeroPublic)
def update_hero(
    hero_id: Annotated[int, Path(gt=0)],
    hero: HeroUpdate,
    session: SessionDep,
):
    return hero_service.update_hero(
        session=session,
        hero_id=hero_id,
        hero_update=hero,
    )


# Delete Hero
@app.delete("/heroes/{hero_id}")
def delete_hero(
    hero_id: Annotated[int, Path(gt=0)],
    session: SessionDep,
):
    return hero_service.delete_hero(
        session=session,
        hero_id=hero_id,
    )