from django.core.cache import cache

USER_CACHE_PATTERN = '{username}'


def invalidate_user_cache(username):
    cache_key = USER_CACHE_PATTERN.format(username=username)
    cache.delete(cache_key)
