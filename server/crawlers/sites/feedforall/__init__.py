def get_site(**kwargs):
    from .site import FeedForAll
    return FeedForAll(**kwargs)