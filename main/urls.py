from django.urls import path

from main.views import index, iha_list, iha_add, iha_rent, my_rental,iha_remove,iha_sil,iha_edit

app_name = "main"

urlpatterns = [
    path("", index, name="main"),
    path("iha-list", iha_list, name="IHA_listeleme"),
    path("iha-add/", iha_add, name="iha_add"),
    path("iha-sil/<int:iha_id>", iha_sil, name="iha_sil"),
    path("iha-guncelle/<int:iha_id>", iha_edit, name="iha_guncelle"),
    path("iha-kirala/<int:iha_id>", iha_rent, name="iha_kirala"),
    path("iha-kira/sil/<int:iha_id>", iha_remove, name="iha_remove"),
    path("ihalarım/", my_rental, name="my_rental"),



]
