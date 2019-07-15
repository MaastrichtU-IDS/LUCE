from django.contrib import admin
from django.urls import path

# Import generic logout view
from django.contrib.auth.views import LogoutView

# Import settings to access environment variables 
from django.conf import settings

# Import view functions here
from lucehome.views import (
    home_page,
    dev_view,
    # register_view,
    RegisterView,
    LoginView,
    LoginView_PostReg,
    )

from datastore.views import (
	upload_view,
	browse_view,
    my_data_view,
    detail_view,
    update_view,
    # UpdateView,
    delete_view,
	)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home_page),
    path('upload/', upload_view),
    path('browse/', browse_view),
    path('my_data/', my_data_view),
    path('dev/', dev_view),
    path('search/', home_page),

    # path('register/', register_view),
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),

    # Post Registration/Upload Views
    path('register_login/', LoginView_PostReg.as_view()),
    # path('upload_success/', ),

    

    path('data/<int:dataset_id>/', detail_view),
    path('data/<int:dataset_id>/edit', update_view),
    path('data/<int:dataset_id>/delete', delete_view),
    # re_path(r'^data/(?P<slug>\w+)/$', detail_view)

]

if settings.DEBUG:
    # Use local simulated CDN
    # Add the following to urlpatterns
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
