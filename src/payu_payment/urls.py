
# from django
from django.urls import path

# from Views
from .views import LogList, CreateLog

app_name = 'payu'

urlpatterns = [
    path('log/', LogList.as_view(), name='log_list'),
    path('confirmation/', CreateLog.as_view(), name='confirmation'),
]