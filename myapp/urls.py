from django.contrib import auth
from django.contrib.auth.forms import SetPasswordForm
from django.urls import path
from django.utils.translation import templatize
from myapp import views
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from .views import  MyLoginView, PasswordChange, show_cart
# from django.contrib.auth.forms import SetPasswordForm
from .forms import MyPasswordResetForm, MySetPasswordForm
urlpatterns = [
    path('', views.home),
    path('home/', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('misc-products/', views.miscellaneousProduct, name='miscellaneous-products'),
    path('groc-products/', views.groceryProduct, name='grocery-products'),
    path('milk-products/', views.milkProduct, name='milk-products'),
    path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('sign-up/', views.SignUpView.as_view(), name='sign_up'),
    path('login/', MyLoginView.as_view(), name='log_in'),
    path('logout/' , auth_views.LogoutView.as_view(next_page = 'log_in'), name='log_out'),
    path('add-address/', views.AddAddressView.as_view(), name='add_address'),
    path('password-change/', PasswordChange.as_view(), name='password_change'),
    path('passwordchangedone/', auth_views.PasswordChangeDoneView.as_view(template_name='passwordChangeDone.html'), name='password_change_done'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='passwordreset.html', form_class=MyPasswordResetForm), name='password_reset'),
    path('password-reset-done/', auth_views.PasswordResetDoneView.as_view(template_name='passwordresetdone.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='passwordresetconfirm.html', form_class=MySetPasswordForm), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='passwordresetcomplete.html'), name='password_reset_complete'),
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.show_cart, name='show_cart'),
    path('pluscart/', views.plus_cart),
    path('minuscart/', views.minus_cart),
    path('removecart/', views.remove_cart),
    path('checkout/', views.checkout, name='checkout'),
    path('orders/', views.orders, name='orders'),
    path('payment-done/', views.payment_done, name='payment_done'),
    path('profile/', views.profile, name='profile'),
    path('payment/', views.payment, name='payment'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)