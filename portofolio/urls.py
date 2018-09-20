from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import jobs.views
import wordcount.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', jobs.views.home, name='home'),
    #initial 'blog' is whatever you want, inlude('<nameofApp>.urls')
    #path('job/', inlude('jobs.urls')),
    path('blog/', include('blog.urls')),
    path('wordcount/', include('wordcount.urls')),
    # path('wordcount/', wordcount.views.wordcount, name='wordcount'),
    # path('wordcount/count', wordcount.views.count, name='count'),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
