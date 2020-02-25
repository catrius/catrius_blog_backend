from math import ceil

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CountedPageNumberPagination(PageNumberPagination):
    def get_paginated_response(self, data):
        count = self.page.paginator.count
        return Response({
            'count': count,
            'page_count': ceil(self.page.paginator.count / self.page_size),
            'results': data,
        })
