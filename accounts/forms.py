from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelChoiceField

from accounts.models import StudentInformation
from school_teachers.models import School


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    school = ModelChoiceField(queryset=School.objects.all())
    grade = forms.IntegerField()

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "first_name", "last_name")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            school = School.objects.get(id=self.data.get('school'))
            user.studentinformation.school = school
            user.studentinformation.grade = self.data.get('grade')
        return user
