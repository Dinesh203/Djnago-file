from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.blogpost, name="blogpost"),
    path("addblog/", views.addblog, name="addblog"),
    path("deleted/<int:id>", views.deleteblog, name="deleteblog")


]
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




# <a href="/edit/{{ employee.id }}"><span class="glyphicon glyphicon-pencil" >Edit</span></a>  
