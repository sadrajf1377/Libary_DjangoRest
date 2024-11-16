from rest_framework.pagination import PageNumberPagination





class Book_Pagination(PageNumberPagination):
    page_size = 100
    page_query_param = 'page_size'