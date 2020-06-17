from django.views.decorators.csrf import csrf_exempt
from django.http import QueryDict
from utils.HTTPUtils import HTTPUtils
from crawlers.models import Feed
import logging
logger = logging.getLogger('crawlers')


@csrf_exempt
def main(request):
    if request.method == 'GET':
        feed_id = request.GET.get('feedId', None)
        if feed_id:
            return get_by_id(request)
        else:
            return get_feeds(request)
    # in order to re-use code, we merge the POST and PUT method together
    elif request.method == 'POST':
        return create_or_update_feed(request)
    elif request.method == 'DELETE':
        return delete_feed(request)
    else:
        return HTTPUtils.format_data_for_api({"status": "Invalid method"})


# GET method
def get_by_id(request):
    feed_id = request.GET.get('feedId', None)
    # we can check the logic for authorization in here
    feed = Feed.get_by_id(feed_id)
    result = feed.to_json() if feed else {}
    return HTTPUtils.format_data_for_api(result)


# GET method
def get_feeds(request):
    page = request.GET.get('page', 0)
    page_size = request.GET.get('pageSize', 0)
    filter_keyword = request.GET.get('filterKeyword', 0)
    if not page_size.isdigit() or not page.isdigit():
        return HTTPUtils.format_data_for_api({'status': 'page & page size must be numeric'})
    return HTTPUtils.format_data_for_api(Feed.get_all(int(page), int(page_size), filter_keyword))


# POST & PUT method
def create_or_update_feed(request):
    feed_id = request.POST.get('feedId', None)
    source = request.POST.get('source', None)
    title = request.POST.get('title', None)
    description = request.POST.get('description', None)
    url = request.POST.get('url', None)
    if not source or not title or not description:
        return HTTPUtils.format_data_for_api({'status': 'All required fields need to be input'})
    return HTTPUtils.format_data_for_api({"status": Feed.create_or_update(source, title, description, url, feed_id)})


# DELETE method
def delete_feed(request):
    feed_id = QueryDict(request.body).get('feedId', None)
    return HTTPUtils.format_data_for_api({'status': Feed.delete_by_id(feed_id)})


def get_all_sources(request):
    sources = Feed.get_all_sources()
    new_sources = [{"value": source, "text": source} for source in sources]
    return HTTPUtils.format_data_for_api({"sources": new_sources})