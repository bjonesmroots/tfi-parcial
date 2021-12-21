# -*- coding: utf-8 -*-

from odoo import models, fields


class Inquilino(models.Model):
    _name = 'realty.inquilino'
    _description = 'Inquilinos de contratos'

    contacto = fields.Many2one('realty.contacto', 'Inquilino')
    contrato = fields.Many2one('realty.contrato', 'Contrato')
    nombre = fields.Char(related='contacto.nombre', string='Nombre', )
    dni = fields.Char(related='contacto.dni', string='DNI', )

    def name_get(self):
        result = []
        for record in self:
            result.append((record.id, record.contact.nombre))
        return result
