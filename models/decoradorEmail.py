from .decoradorNotificacion import DecoradorNotificacion


class DecoradorEmail(DecoradorNotificacion):

    def enviarNotificacion(self) -> bool:
        print('Email enviado a ' + self.originalComponent.message_email_to + ': ' + self.originalComponent.message_body)
        DecoradorEmail({self.component.enviarNotificacion()})
        return True
