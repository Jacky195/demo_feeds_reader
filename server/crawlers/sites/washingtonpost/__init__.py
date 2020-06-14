def get_site(**kwargs):
    from .site import WashingtonPostSite
    return WashingtonPostSite(**kwargs)