from app.core.config import settings

def test_settings_loaded():
    assert settings.DATABASE_URL is not None
    assert settings.SECRET_KEY is not None