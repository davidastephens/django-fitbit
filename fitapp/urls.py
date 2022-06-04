from django.urls import path, re_path

from . import views


urlpatterns = [
    # OAuth authentication
    path('login/', views.login, name='fitbit-login'),
    path('complete/', views.complete, name='fitbit-complete'),
    path('error/', views.error, name='fitbit-error'),
    path('logout/', views.logout, name='fitbit-logout'),

    # Subscriber callback for near realtime updates
    path('update/', views.update, name='fitbit-update'),

    # Fitbit data retrieval
    re_path(r'^get_data/(?P<category>[\w]+)/(?P<resource>[/\w]+)/$',
        views.get_data, name='fitbit-data'),
    path('get_steps/', views.get_steps, name='fitbit-steps')
]
