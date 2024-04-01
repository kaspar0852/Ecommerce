from rest_framework import pagination
from rest_framework.response import Response


class LargeResultsPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

    # def get_paginated_response(self, data):
    #     return Response({
    #         'links': {
    #             'next': self.get_next_link(),
    #             'previous': self.get_previous_link()
    #         },
    #         'count': self.page.paginator.count,  # Use 'page.paginator.count' for total items
    #         'total_pages': self.page.paginator.num_pages,  # Use 'page.paginator.num_pages' for total pages
    #         'results': data
    #     })