from rest_framework.pagination import PageNumberPagination
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.pagination import CursorPagination


class MyPageNumberPagination(PageNumberPagination):

    # 每页显示多少个
    page_size = 3
    # 默认每页显示3个，可以通过传入pager1/?page=2&size=4,改变默认每页显示的个数
    page_size_query_param = "size"
    # 最大页数不超过10
    max_page_size = 10
    # 获取页码数的
    page_query_param = "page"


#自定义分页类2
class MyLimitOffsetPagination(LimitOffsetPagination):
    #默认显示的个数
    default_limit = 2
    #当前的位置
    offset_query_param = "offset"
    #通过limit改变默认显示的个数
    limit_query_param = "limit"
    #一页最多显示的个数
    max_limit = 10




class MyCursorPagination(CursorPagination):
    cursor_query_param = "cursor"
    page_size = 2     #每页显示2个数据
    ordering = 'id'   #排序
    page_size_query_param = None
    max_page_size = None