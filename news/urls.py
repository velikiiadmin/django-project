from django.urls import path
from .views import *

urlpatterns = [
    # Контроллер функции
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('loginout/', user_logout, name='logout'),
    path('sendmail/', email_send, name='sendmail'),
    # path('', index, name='home'),
    # Контроллер класс
    path('', HomeNews.as_view(), name='home'),
    # path('category/<int:category_id>', get_category, name='category'),
    path('category/<int:category_id>', NewsByCategory.as_view(), name='category'),
    # path('news/<int:news_id>', view_news, name='view_news'),
    path('news/<int:pk>', ViewNews.as_view(), name='view_news'),
    # path('news/add-news/', add_news, name='add_news'),
    path('news/add-news/', CreateNews.as_view(), name='add_news'),
]

