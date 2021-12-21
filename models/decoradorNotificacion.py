from odoo import models


class DecoradorNotificacion():
    _component: models.Model = None

    def __init__(self, component: models.Model) -> None:
        self._component = component

    @property
    def component(self) -> bool:
        return self._component

    @property
    def originalComponent(self):
        superComponent = self
        while hasattr(superComponent, 'component'):
            superComponent = superComponent.component
        return superComponent

    def enviarNotificacion(self) -> bool:
        return self._component.enviarNotificacion()
