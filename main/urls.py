from django.urls import path

from main.views import index, iha_list

app_name = "main"

urlpatterns = [
    path("", index, name="main"),
    path("iha-list", iha_list, name="IHA_listeleme"),



]
