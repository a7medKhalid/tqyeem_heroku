from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms.models import ModelForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username','email','address',)
        


class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = CustomUser
        fields = ('address',)


# class addReview(forms.Form):
#     ratingText = 

# class ProductForm(forms.ModelForm):

#     class Meta:
#         model = Product

#         fields = [
#             "productId"
#         ]


# class ApprovedSellerForm(forms.ModelForm):

#     class Meta:
#         model = ApprovedSeller

#         fields = [
#             "name",
#             "url"
#         ]