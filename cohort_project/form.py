from django.forms import ModelForm

from cohort_project.models import Cohort, Native, Login


class CohortForm(ModelForm):
    class Meta:
        model = Cohort
        fields = ('name', 'description')


class NativeForm(ModelForm):
    class Meta:
        model = Native
        fields = ('image', 'first_name', 'last_name', 'cohort', 'scv')


class LoginForm(ModelForm):
    class Meta:
        model = Login
        fields = ('email', 'password')
