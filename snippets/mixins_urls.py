from django.conf.urls import url
from . import views
from . import apiview
from . import mixins_view
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # 实例化对象时处理python对象，返回json数据
    # url(r'^snippets/$', views.JSONResponse.snippet_list),
    # url(r'^snippets/(?P<pk>[0-9]+)/$', views.JSONResponse.snippet_detail),


    # 用rest_framework.response  Response返回json数据
    url(r'^snippets/$', mixins_view.SnippetList.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)/$', mixins_view.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
