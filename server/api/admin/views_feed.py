from utils.HTTPUtils import HTTPUtils
from crawlers.models import Feed


def main(request):
    if request.method == 'GET':
        return get_feeds(request)


def get_feeds(request):
    page = request.GET.get('page', 0)
    page_size = request.GET.get('pageSize', 0)
    filter_keyword = request.GET.get('filterKeyword', 0)

    if not page_size.isdigit() or not page.isdigit():
        return HTTPUtils.format_data_for_ajax({'status': 'page & page size must be numeric'})

    return HTTPUtils.format_data_for_ajax({
        'feeds': Feed.get_all(int(page), int(page_size), filter_keyword)
    })