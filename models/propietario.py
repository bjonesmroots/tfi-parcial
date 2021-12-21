# -*- coding: utf-8 -*-

from odoo import models, fields


class Propietario(models.Model):
    _name = 'realty.propietario'
    _description = 'Propetarios de propiedades'

    contacto = fields.Many2one('realty.contacto', 'Propietario')
    propiedad = fields.Many2one('realty.propiedad', 'Propiedad')

    def name_get(self):
        result = []
        for record in self:
            result.append((record.id, record.contact.nombre))
        return result
