# Simple Django App

A simple Django application with file upload functionality and health check endpoint.

## Features

- File upload functionality
- Health check endpoint for readiness probes
- Django REST Framework integration

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run migrations:
```bash
python manage.py migrate
```

3. Start the development server:
```bash
python manage.py runserver
```

## API Endpoints

### Health Check
- **URL**: `/health/`
- **Method**: `GET`
- **Description**: Readiness probe endpoint that returns HTTP 200 OK
- **Authentication**: None required

### File Upload
- **URL**: `/upload/`
- **Method**: `POST`
- **Description**: Upload files to the server
- **Authentication**: None required

## Project Structure

```
simple-django-app/
├── app/                    # Main Django project settings
│   ├── settings.py        # Django settings
│   ├── urls.py           # Main URL configuration
│   └── wsgi.py           # WSGI configuration
├── uploader/              # Main application
│   ├── views.py          # Views including health check endpoint
│   ├── urls.py           # Application URL configuration
│   └── models.py         # Database models
├── requirements.txt       # Python dependencies
├── manage.py             # Django management script
└── README.md             # This file
```

## Health Check Endpoint

The health check endpoint is implemented as a Django REST Framework ViewSet:

```python
class GeneralViewSet(GenericViewSet):
    permission_classes = [AllowAny]

    @action(detail=False, methods=['GET'], url_path='health')
    def health(self, request):
        return Response(status=status.HTTP_200_OK)
```

This endpoint is perfect for Kubernetes readiness probes and other health monitoring systems.

## Dependencies

- Django 5.2.4
- Django REST Framework 3.14.0
- asgiref 3.9.0
- sqlparse 0.5.3 