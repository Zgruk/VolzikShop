from email import message
from celery import Task
from django.core.mail import send_mail
from .models import Order

@Task
def order_created(order_id):
    """
    Task to send an e-mail notification when order is
    successfully created.
    """
    order = Order.objects.get(id=order_id)
    subject = f'Заказ № {order.id}'
    message = f'Дорогой {order.first_name}, \n\n' \
              f'Вы успешно разместили заказ.' \
              f'Ваш номер заказа - {order.id}.'
    mail_sent = send_mail(subject,
                          message,
                          'admin@VolzikShop.com',
                          [order.email])
    return mail_sent