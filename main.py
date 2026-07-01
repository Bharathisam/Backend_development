from typing import Annotated

from fastapi import Depends, FastAPI, Path, Query, status
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session, SQLModel, create_engine

from core.exception_handler import register_exception_handlers
from models import HeroCreate, HeroPublic, HeroUpdate
from services import hero_service

# -----------------------------
# Database Configuration
# -----------------------------
sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)


# -----------------------------
# Create Database Tables
# -----------------------------
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


# -----------------------------
# Database Session Dependency
# -----------------------------
def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]


# -----------------------------
# FastAPI App
# -----------------------------
app = FastAPI(
    title="Hero Management API",
    description="FastAPI Learning Project - Stage 8: Handoff & Integration Support",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    contact={
        "name": "Bharathi S",
        "url": "https://github.com/Bharathisam/Backend_development",
    },
    license_info={
        "name": "MIT License",
    },
)

# -----------------------------
# Register Global Exception Handlers
# -----------------------------
register_exception_handlers(app)


# -----------------------------
# CORS Configuration
# -----------------------------
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# -----------------------------
# Startup Event
# -----------------------------
@app.on_event("startup")
def on_startup():
    create_db_and_tables()


# -----------------------------
# Create Hero
# -----------------------------
@app.post(
    "/heroes/",
    response_model=HeroPublic,
    status_code=status.HTTP_201_CREATED,
)
def create_hero(
    hero: HeroCreate,
    session: SessionDep,
):
    return hero_service.create_hero(session, hero)


# -----------------------------
# Get All Heroes
# -----------------------------
@app.get(
    "/heroes/",
    response_model=list[HeroPublic],
    status_code=status.HTTP_200_OK,
)
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


# -----------------------------
# Get Hero by ID
# -----------------------------
@app.get(
    "/heroes/{hero_id}",
    response_model=HeroPublic,
    status_code=status.HTTP_200_OK,
)
def read_hero(
    hero_id: Annotated[int, Path(gt=0)],
    session: SessionDep,
):
    return hero_service.read_hero(
        session=session,
        hero_id=hero_id,
    )


# -----------------------------
# Update Hero
# -----------------------------
@app.patch(
    "/heroes/{hero_id}",
    response_model=HeroPublic,
    status_code=status.HTTP_200_OK,
)
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


# -----------------------------
# Delete Hero
# -----------------------------
@app.delete(
    "/heroes/{hero_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_hero(
    hero_id: Annotated[int, Path(gt=0)],
    session: SessionDep,
):
    hero_service.delete_hero(
        session=session,
        hero_id=hero_id,
    )