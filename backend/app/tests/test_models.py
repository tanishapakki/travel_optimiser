from app.core.db import engine

def test_engine_created():
    assert engine is not None