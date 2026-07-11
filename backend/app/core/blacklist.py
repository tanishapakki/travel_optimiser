from app.core.redis import redis_client

def blacklist_token(jti: str, ttl: int):
    """
    Blacklists a JWT token by storing its JTI in Redis with an expiration time.

    Args:
        jti (str): The JTI of the token to blacklist.
        ttl (int): The time-to-live in seconds for the blacklisted token.
    """
    redis_client.setex(f"blacklisted:{jti}", ttl, "blacklisted")

def is_blacklisted(jti: str) -> bool:
    """
    Checks if a JWT token is blacklisted by looking up its JTI in Redis.

    Args:
        jti (str): The JTI of the token to check.
        """
    return redis_client.exists(f"blacklisted:{jti}") == 1











