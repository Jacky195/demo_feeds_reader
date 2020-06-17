from django.views.decorators.csrf import csrf_exempt
from utils.HTTPUtils import HTTPUtils
from crawlers.models import Feed
import logging
logger = logging.getLogger('crawlers')


@csrf_exempt
def main(request):
    if request.method == 'GET':
        return get_feeds(request)
    elif request.method == 'POST':
        return create_feed(request)


def get_feeds(request):
    page = request.GET.get('page', 0)
    page_size = request.GET.get('pageSize', 0)
    filter_keyword = request.GET.get('filterKeyword', 0)

    if not page_size.isdigit() or not page.isdigit():
        return HTTPUtils.format_data_for_api({'status': 'page & page size must be numeric'})

    return HTTPUtils.format_data_for_api(Feed.get_all(int(page), int(page_size), filter_keyword))


def create_feed(request):
    source = request.POST.get('source', None)
    title = request.POST.get('title', None)
    description = request.POST.get('description', None)
    url = request.POST.get('url', None)

    if not source or not title or not description:
        return HTTPUtils.format_data_for_api({'status': 'All required fields need to be input'})

    return HTTPUtils.format_data_for_api({"status": Feed.create(source, title, description, url)})


def get_all_sources(request):
    sources = Feed.get_all_sources()
    new_sources = [{"value": source, "text": source} for source in sources]
    return HTTPUtils.format_data_for_api({"sources": new_sources})