from io import BytesIO
from celery import shared_task
import weasyprint
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from orders.models import Order


@shared_task
def payment_completed(order_id):
    """
    Task to send an e-mail notification when an order is
    successfully created."""
    order = Order.objects.get(id=order_id)

    # create invoice e-mail
    subject = f'VolzikShop - EE Счет № {order.id}'
    message = f'Уважаемый покупатель, в прикрепленном файле вы найдете счет на вашу недавнюю покупку.'
    email = EmailMessage(subject,
                         message,
                         'admin@VolzikShop.com',
                         [order.email])
    # generate PDF
    html = render_to_string('orders/order/pdf.html', {'order': order})
    out = BytesIO()
    stylesheets=[weasyprint.CSS(settings.STATIC_ROOT + 'css/pdf.css')]
    weasyprint.HTML(string=html).write_pdf(out, stylesheets=stylesheets)

    # attach PDF file
    email.attach(f'Заказ_{order.id}.pdf',
                 out.getvalue(),
                 'application/pdf')

    # send an e-mail
    email.send()
