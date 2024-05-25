from rest_framework.pagination import PageNumberPagination
from urllib.parse import urlencode
from rest_framework.response import Response

class CustomPagination(PageNumberPagination):
    page_size = 10  # Set the number of items per page
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data #sadsadsad
        })

    def get_next_link(self):
        if not self.page.has_next():
            return None
        page_number = self.page.next_page_number()
        return self._get_link(page_number)

    def get_previous_link(self):
        if not self.page.has_previous():
            return None
        page_number = self.page.previous_page_number()
        return self._get_link(page_number)

    def _get_link(self, page_number):
        url = self.request.build_absolute_uri()
        query_params = self.request.query_params.copy()
        query_params['page'] = page_number
        return '{}?{}'.format(url.split('?')[0], urlencode(query_params))
