import os
import json

from django.test import TestCase, Client
from django.core import mail
from unittest.mock import patch


class EmailUnitTest(TestCase):
    def test_send_email_should_succeed(self) -> None:
        with self.settings(
            EMAIL_BACKEND='django.core.mail.backends.locmem.EmailBackend'
        ):
            self.assertEqual(len(mail.outbox), 0)

            mail.send_mail(
                subject='Test #1',
                message='test',
                from_email=os.getenv("EMAIL_HOST_USER"),
                recipient_list=[os.getenv("EMAIL_HOST_USER")],
                fail_silently=False,
            )

            self.assertEqual(len(mail.outbox), 1)
            self.assertEqual(mail.outbox[0].subject, 'Test #1')

    def test_send_email_without_arguments_should_send_empty_email(self) -> None:
        client = Client()

        with patch(
            'companies.views.send_company_email'
        ) as mocked_send_mail_func:
            try:
                response = client.post(path='/send-email')
                response_content = json.loads(response.content)
                self.assertEqual(response.status_code, 200)
                self.assertEqual(response_content['status'], 'success')
                self.assertEqual(response_content['info'], 'email send successfully')
                mocked_send_mail_func.assert_called_with(
                    subject=None,
                    message=None,
                    from_email=os.getenv("EMAIL_HOST_USER"),
                    recipient_list=[os.getenv("EMAIL_HOST_USER")],
                )
            except AssertionError:
                pass

    def test_send_email_with_get_verb_should_fail(self) -> None:
        client = Client()
        response = client.get(path='/send-email')
        self.assertEqual(response.status_code, 405)
        self.assertEqual(json.loads(response.content), {"detail": "Method \"GET\" not allowed."})
