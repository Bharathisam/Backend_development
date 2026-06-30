from fastapi import HTTPException

from models import Hero
from repository import hero_repository


def create_hero(session, hero):
    db_hero = Hero.model_validate(hero)
    return hero_repository.create_hero(session, db_hero)


def read_heroes(session, offset, limit):
    return hero_repository.get_all_heroes(session, offset, limit)


def read_hero(session, hero_id):
    hero = hero_repository.get_hero_by_id(session, hero_id)

    if not hero:
        raise HTTPException(
            status_code=404,
            detail="Hero not found"
        )

    return hero


def update_hero(session, hero_id, hero_update):
    hero = hero_repository.get_hero_by_id(session, hero_id)

    if not hero:
        raise HTTPException(
            status_code=404,
            detail="Hero not found"
        )

    hero_data = hero_update.model_dump(exclude_unset=True)
    hero.sqlmodel_update(hero_data)

    return hero_repository.update_hero(session, hero)


def delete_hero(session, hero_id):
    hero = hero_repository.get_hero_by_id(session, hero_id)

    if not hero:
        raise HTTPException(
            status_code=404,
            detail="Hero not found"
        )

    hero_repository.delete_hero(session, hero)

    return {"ok": True}