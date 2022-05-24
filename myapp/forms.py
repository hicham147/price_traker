from django import forms
from .models import Link,Amazon,Niceone,Xcite

class AddLinkform(forms.ModelForm):
    class Meta:
        model = Link
        fields = ('url',)


class AmazonAddlink(forms.ModelForm):
    class Meta:
        model = Amazon
        fields = ('url',)


class NiceoneAddlink(forms.ModelForm):
    class Meta:
        model = Niceone
        fields = ('url',)
        
        
class XciteAddlink(forms.ModelForm):
    class Meta:
        model = Xcite
        fields = ('url',)