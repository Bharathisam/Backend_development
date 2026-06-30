from sqlmodel import Field, SQLModel


class HeroBase(SQLModel):
    name: str = Field(
        min_length=3,
        max_length=50,
        index=True
    )

    age: int | None = Field(
        default=None,
        ge=1,
        le=120,
        index=True
    )


class Hero(HeroBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

    secret_name: str = Field(
        min_length=3,
        max_length=100
    )


class HeroCreate(HeroBase):
    secret_name: str = Field(
        min_length=3,
        max_length=100
    )


class HeroPublic(HeroBase):
    id: int


class HeroUpdate(SQLModel):
    name: str | None = Field(
        default=None,
        min_length=3,
        max_length=50
    )

    age: int | None = Field(
        default=None,
        ge=1,
        le=120
    )

    secret_name: str | None = Field(
        default=None,
        min_length=3,
        max_length=100
    )