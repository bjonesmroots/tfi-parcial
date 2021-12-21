from .decoradorNotificacion import DecoradorNotificacion


class DecoradorSMS(DecoradorNotificacion):

    def enviarNotificacion(self) -> bool:
        print('SMS enviado a ' + self.originalComponent.message_sms_to + ': ' + self.originalComponent.message_body)
        DecoradorSMS({self.component.enviarNotificacion()})
        return True
