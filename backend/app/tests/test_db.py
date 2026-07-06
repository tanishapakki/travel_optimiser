from app.core.db import get_db


def test_db():

    db = next(get_db())

    print(db)

    db.close()