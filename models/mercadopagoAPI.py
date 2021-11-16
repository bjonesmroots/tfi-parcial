import string
import random

# Simulacion de llamado a apis de mercado pago


class MercadoPagoAPI:
    @staticmethod
    def validarTarjeta(tarjeta):
        return True

    @staticmethod
    def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    @staticmethod
    def procesarSuscripcion(tarjeta):
        return MercadoPagoAPI.id_generator(size=20)
