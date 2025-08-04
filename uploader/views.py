import os
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from .forms import UploadFileForm

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            file_path = os.path.join(settings.MEDIA_ROOT, uploaded_file.name)
            with open(file_path, 'wb+') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)
            return HttpResponse('File uploaded successfully! Path: {}'.format(file_path))
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})


class GeneralViewSet(GenericViewSet):
    permission_classes = [AllowAny]

    @action(detail=False, methods=['GET'], url_path='health')
    def health(self, request):
        return Response(status=status.HTTP_200_OK)
