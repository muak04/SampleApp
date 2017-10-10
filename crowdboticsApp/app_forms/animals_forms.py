from django import forms

from crowdboticsApp.models import Dog, Cat


class DogForm(forms.ModelForm):
    class Meta:
        model = Dog
        fields = ['name', 'birthday', ]
        widgets = {
            'birthday': forms.SelectDateWidget(),
        }

        widget = forms.SelectDateWidget()

    def __init__(self, *args, **kwargs):
        super(DogForm, self).__init__(*args, **kwargs)


class CatForm(forms.ModelForm):
    class Meta:
        model = Cat
        fields = ['name', 'birthday', ]
        widgets = {
            'birthday': forms.SelectDateWidget(),
        }

    def __init__(self, *args, **kwargs):
        super(CatForm, self).__init__(*args, **kwargs)