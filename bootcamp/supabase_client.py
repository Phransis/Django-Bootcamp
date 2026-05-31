from functools import lru_cache

from django.conf import settings
from supabase import Client, create_client


@lru_cache(maxsize=1)
def get_supabase_client() -> Client:
    url = settings.SUPABASE_URL
    key = settings.SUPABASE_KEY
    if not url or not key:
        raise RuntimeError(
            'SUPABASE_URL and SUPABASE_KEY must be set in environment variables.'
        )
    return create_client(url, key)
