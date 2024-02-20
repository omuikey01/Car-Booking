from django.urls import path
from .views import *


urlpatterns = [
    path("", homepage, name=""),
    path("all-show/", allshow, name="all-show"),
    path("drop-search/", drop_search, name="drop-search"),
    path("map-single-detail/", map_single_detail, name="map-single-detail" ),
    path("product-details/", product_details, name="product-details"),
    path("book-now", book_now, name="book-now"),
    path("payment-done", payment_done, name="payment-done"),
    path("auth/", auth, name="auth"),
    path("about/", about, name="about"),
    path("forgotpass/", forgotpass, name="forgotpass"),
    # path("forgotpass_otp/", forgotpass_otp, name="forgotpass_otp"),
    # path("forgotpass_newpass/", forgotpass_newpass, name="forgotpass_newpass"),
    path("auth_form_up/", auth_form_up, name="auth_form_up"),
    path("auth_form_in/", auth_form_in, name="auth_form_in"),
    path("registerform/", registerform, name="registerform"),
    path("loginform/", loginform, name="loginform"),
]
