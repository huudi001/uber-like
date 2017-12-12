from django.forms import *
from django.conf import settings

class UploadFileForm(forms.Form):
    file = forms.FileField()

    def handle_uploaded_file(self,file):
        
        destination = open(settings.MEDIA_ROOT +'okok', 'wb+')
        for chunk in file.chunks():
            destination.write(chunk)
