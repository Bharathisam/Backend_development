from sqlmodel import Session, select

from models import Hero


def create_hero(session: Session, hero: Hero):
    session.add(hero)
    session.commit()
    session.refresh(hero)
    return hero


def get_all_heroes(session: Session, offset: int, limit: int):
    return session.exec(
        select(Hero).offset(offset).limit(limit)
    ).all()


def get_hero_by_id(session: Session, hero_id: int):
    return session.get(Hero, hero_id)


def update_hero(session: Session, hero: Hero):
    session.add(hero)
    session.commit()
    session.refresh(hero)
    return hero


def delete_hero(session: Session, hero: Hero):
    session.delete(hero)
    session.commit()