from django.conf import settings


class Cart(object):
    def __init__(self, request):
        """
        Initialize the cart
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        # save an empty cart in the session
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
