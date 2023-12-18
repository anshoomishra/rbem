from django.test import TestCase
from notification.aws_sns import send_sms
from django.conf import settings
# Create your tests here.

class PublishMessageTest(TestCase):
    def setUp(self):
        pass

    def test_send_message(self):
        print(settings.AWS_REGION)
        message = send_sms("Hi","6394389266")
        print(message)
        self.assertEqual(1,1)
        return message