from django import http

XS_SHARING_ALLOWED_ORIGINS = '*'
XS_SHARING_ALLOWED_METHODS = ['POST', 'GET', 'OPTIONS', 'PUT', 'DELETE']


class AllowCrossDomainApi:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        response = self.get_response(request)
        response["Access-Control-Allow-Origin"] = "*"

        return response

        #
        # if 'HTTP_ACCESS_CONTROL_REQUEST_METHOD' in request.META:
        #     response = http.HttpResponse()
        #     response['Access-Control-Allow-Origin'] = XS_SHARING_ALLOWED_ORIGINS
        #     response['Access-Control-Allow-Methods'] = ",".join(XS_SHARING_ALLOWED_METHODS)
        #     return response
        # response = self.get_response(request)
        # if response.has_header('Access-Control-Allow-Origin'):
        #     return response
        # response['Access-Control-Allow-Origin'] = XS_SHARING_ALLOWED_ORIGINS
        # response['Access-Control-Allow-Methods'] = ",".join(XS_SHARING_ALLOWED_METHODS)
        # return response
