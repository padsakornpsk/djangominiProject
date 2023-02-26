from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from Profileapp.models import *


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254,
        required=True,
        help_text='Required. Enter a valid email address.',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    # class Meta:
    #     model = User
    #     fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class AddForm(forms.ModelForm):
    class Meta:
        model = Contents
        fields = (
        'cont_id', 'cont_name', 'content', 'cont_address', 'cont_image', 'cont_date', 'cont_phonenumber', 'cont_email',
        'cat_id')
        widgets = {
            'cont_id': forms.TextInput(attrs={'class': 'form-control'}),
            'cont_name': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'cont_address': forms.Textarea(attrs={'class': 'form-control'}),
            'cont_image': forms.FileInput(attrs={'class': 'form-control', 'accept': 'image/Content/*'}),
            'cont_date': forms.NumberInput(attrs={'class': 'form-control', 'type': 'date'}),
            'cont_phonenumber': forms.TextInput(attrs={'class': 'form-control'}),
            'cont_email': forms.TextInput(attrs={'class': 'form-control'}),
            'cat_id': forms.Select(attrs={'class': 'form-control'})

        }
        labels = {
            'cont_id': 'รหัสเนื้อหา',
            'cont_name': 'ชื่อโรงแรม',
            'content': 'เนื้อหา',
            'cont_address': 'ที่อยู่',
            'cont_image': 'รูปภาพ',
            'cont_date': 'วันที่ลงเนื้อหา',
            'cont_phonenumber': 'เบอร์โทรศัพท์ติดต่อ',
            'cont_email': 'อีเมลล์ติดต่อ',
            'cat_id': 'หมวดหมู่เนื้อหา',

        }

    def updateForm(self):
        self.fields['cont_id'].widget.attrs['readonly'] = True

    def deleteForm(self):
        self.fields['cont_id'].widget.attrs['readonly'] = True
        self.fields['cont_name'].widget.attrs['readonly'] = True
        self.fields['content'].widget.attrs['readonly'] = True
        self.fields['cont_address'].widget.attrs['readonly'] = True
        self.fields['cont_image'].widget.attrs['readonly'] = True
        self.fields['cont_date'].widget.attrs['readonly'] = True
        self.fields['cont_phonenumber'].widget.attrs['readonly'] = True
        self.fields['cont_email'].widget.attrs['readonly'] = True
        self.fields['cat_id'].widget.attrs['readonly'] = True

# class RegisterForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('uid','name', 'address', 'tel',)
#         widgets = {
#             'uid': forms.TextInput(attrs={'class': 'form-control', 'size':15, 'maxlength':13}),
#             'name': forms.TextInput(attrs={'class': 'form-control', 'size':55, 'maxlength':50}),
#             'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
#             'tel': forms.TextInput(attrs={'class': 'form-control','size':13, 'maxlength':10}),
#
#         }
#         labels = {
#             'cid': 'รหัสประจำตัว (User Name)',
#             'name': 'ชื่อลูกค้า',
#             'address': 'ที่อยู่',
#             'tel': 'เบอร์โทรศัพท์',
#
#          }
class categoryForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = (
        'cat_id', 'cat_name', 'cat_desc')
        widgets = {
            'cat_id': forms.TextInput(attrs={'class': 'form-control'}),
            'cat_name': forms.TextInput(attrs={'class': 'form-control'}),
            'cat_desc': forms.Textarea(attrs={'class': 'form-control'}),

        }
        labels = {
            'cat_id': 'รหัสหมวดหมู่',
            'cat_name': 'หมวดหมู่',
            'cat_desc': 'คำอธิบาย',

        }

    def updateForm(self):
        self.fields['cat_id'].widget.attrs['readonly'] = True

    def deleteForm(self):
        self.fields['cat_id'].widget.attrs['readonly'] = True
        self.fields['cat_name'].widget.attrs['readonly'] = True
        self.fields['cat_desc'].widget.attrs['readonly'] = True