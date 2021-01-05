from django.urls import path,re_path
from pdf import views

app_name = 'pdf'

urlpatterns = [
    path('generating',views.generating.as_view(),name='generating'),
    path('<int:id>/',views.pdf_detail,name='pdf_detail'),
    path("list",views.list_user.as_view(),name='list_user'),

]
