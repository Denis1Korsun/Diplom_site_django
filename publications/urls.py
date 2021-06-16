from django.urls import path
from .views import about, contact, shop, logout_user, PublicationsHome, PublicationsCategory, ShowPost, RegisterUser, \
    LoginUser, CommunicationFormView, about_authors, about_athlete

urlpatterns = [
    path('', PublicationsHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('addpage/', CommunicationFormView.as_view(), name='add_page'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('contact/', contact, name='contact'),
    path('shop/', shop, name='shop'),
    path('registration/', RegisterUser.as_view(), name='registration'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('rubric/<slug:rubric_slug>/', PublicationsCategory.as_view(), name='rubric'),
    path('about_author/', about_authors, name='about_authors'),
    path('about_athlete/', about_athlete, name='about_athlete')

]
