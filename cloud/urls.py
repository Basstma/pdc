from django.urls import path
from .views import *

urlpatterns = [
    path('', cloud_main, name="cloudmain"),
    path('showfile/<int:id>', cloud_show_content, name='cloud_show_content'),
    path('showembedded/<int:id>', cloud_show_embedded, name='cloud_show_embedded'),
    path('download/<int:id>', cloud_download_content, name='cloud_download'),
    path('addcontent', cloud_add_content, name='cloud_addcontent'),
    path('addembedded', cloud_add_embedded_content, name='cloud_addembedded'),
    path('deletefile/<int:id>', cloud_delete_file, name='cloud_deletefile'),
    path('deleteembedded/<int:id>', cloud_delete_embedded, name='cloud_deleteembedded'),
]