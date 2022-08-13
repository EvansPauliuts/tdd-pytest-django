import os

from django.core.mail import send_mail
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework import status

from companies.serializers import CompanySerializer
from companies.models import Company


class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all().order_by("-last_update")
    serializer_class = CompanySerializer
    pagination_class = PageNumberPagination


@api_view(http_method_names=["POST"])
def send_company_email(request: Request) -> Response:
    send_mail(
        subject=request.data.get('subject'),
        message=request.data.get('message'),
        from_email=os.getenv("EMAIL_HOST_USER"),
        recipient_list=[os.getenv("EMAIL_HOST_USER")],
    )

    return Response(
        {"status": "success", "info": "email send successfully"},
        status=status.HTTP_200_OK,
    )
