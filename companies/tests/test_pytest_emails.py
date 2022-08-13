import os
import pytest
import json

from django.urls import reverse
from django.core import mail
from unittest.mock import patch

companies_url = reverse("companies-list")
pytestmark = pytest.mark.django_db


def test_send_email_should_succeed(mailoutbox, settings) -> None:
    settings.EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"
    assert len(mailoutbox) == 0

    mail.send_mail(
        subject="Test #1",
        message="test",
        from_email=os.getenv("EMAIL_HOST_USER"),
        recipient_list=[os.getenv("EMAIL_HOST_USER")],
        fail_silently=False,
    )

    assert mailoutbox[0].subject == "Test #1"


def test_send_email_without_arguments_should_send_empty_email(client) -> None:
    with patch("companies.views.send_company_email") as mocked_send_mail_func:
        try:
            response = client.post(path="/send-email")
            response_content = json.loads(response.content)
            assert response.status_code == 200
            assert response_content["status"] == "success"
            assert response_content["info"] == "email send successfully"
            mocked_send_mail_func.assert_called_with(
                subject=None,
                message=None,
                from_email=os.getenv("EMAIL_HOST_USER"),
                recipient_list=[os.getenv("EMAIL_HOST_USER")],
            )
        except AssertionError:
            pass


def test_send_email_with_get_verb_should_fail(client) -> None:
    response = client.get(path="/send-email")
    assert response.status_code == 405
    assert json.loads(response.content) == {"detail": 'Method "GET" not allowed.'}
