# -*- coding: utf-8 -*-

from odoo import models, fields


class Garante(models.Model):
    _name = 'realty.garante'
    _description = 'Garantes de contratos'

    contacto_id = fields.Many2one('realty.contacto', 'Garante')
    contrato_id = fields.Many2one('realty.contrato', 'Contrato')
    nombre = fields.Char(related='contacto_id.nombre', string='Nombre', )
    dni = fields.Char(related='contacto_id.dni', string='DNI', )
