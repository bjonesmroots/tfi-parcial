# -*- coding: utf-8 -*-

from odoo import models, fields


class Inquilino(models.Model):
    _name = 'realty.inquilino'
    _description = 'Inquilinos de contratos'

    contacto_id = fields.Many2one('realty.contacto', 'Inquilino')
    contrato_id = fields.Many2one('realty.contrato', 'Contrato')
    nombre = fields.Char(related='contacto_id.nombre', string='Nombre', )
    dni = fields.Char(related='contacto_id.dni', string='DNI', )
