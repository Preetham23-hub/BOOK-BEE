
from django.urls import path
from .views import index,register,signin,entry,enter,home,logout,upload,upload_book,booklist,delete,update,weadd

urlpatterns = [
    path('', index,name='index'),
    path('register/', register,name='register'),
    path('signin/', signin,name='signin'),
    path('entry/', entry,name='entry'),
    path('enter/', enter, name='enter'),
    path('home/',home,name='home'),
    path('logout/',logout,name='logout'),
    path('upload/', upload, name='upload'),
    path('upload_book/', upload_book, name='upload_book'),
    path('booklist/', booklist, name='booklist'),
    path('delete/<int:id>/', delete, name='delete'),
    path('update/<int:id>/', update, name='update'),
    path('added/', weadd, name='weadd')

]
