from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(label='', required=True, max_length=70,
                                 widget=forms.TextInput(
                                     attrs={'class': 'form-control', 'placeholder': 'Имя'}))
    last_name = forms.CharField(label='', required=True, max_length=70,
                                widget=forms.TextInput(
                                    attrs={'class': 'form-control', 'placeholder': 'Фамилия'}))
    email = forms.EmailField(label='', required=True, max_length=70,
                             widget=forms.TextInput(
                                 attrs={'class': 'form-control', 'placeholder': 'Адрес электронной почты'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Имя пользователя'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Обязательное поле. Не более 150 символов. Только буквы, цифры и @/./+/-/_.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Пароль'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Пароль не должен быть похож на другие ваши данные</li><li>Пароль должен быть длиннее 8 символов.</li><li>Пароль не должен быть распространен</li><li>Пароль не может состоять только из цифр</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Повторите пароль'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Введите пароль еще раз.</small></span>'