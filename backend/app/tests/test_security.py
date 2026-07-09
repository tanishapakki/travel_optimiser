from app.core.security import (
    create_access_token,
    decode_access_token,
    hash_password,
    verify_password,
)

from datetime import timedelta

password = "MyPassword123"

hashed = hash_password(password)

print("Hashed Password:")
print(hashed)

print()

print(
    verify_password(
        password,
        hashed,
    )
)

print(
    verify_password(
        "wrongpassword",
        hashed,
    )
)

print()


expired = create_access_token(
    {"sub": "tanisha"},
    expires_delta=timedelta(seconds=-5),
)

try:
    decode_access_token(expired)
except Exception as e:
    print(type(e).__name__)
