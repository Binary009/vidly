from django.urls import path
from . import views

# In this list, we add objects that map url endpoints to view functions
# movies/
# movies/1/detalis
urlpatterns = [
    path('', views.index, name='index') # naming url endpoint
]