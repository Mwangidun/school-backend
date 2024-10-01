from django import forms
from .models import Enrollment, News, Gallery

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['name', 'email', 'level_of_education', 'gender', 'phone_number']
        
class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'

class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = '__all__'
