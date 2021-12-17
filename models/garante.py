# -*- coding: utf-8 -*-

from odoo import models, fields


class Garante(models.Model):
    _name = 'realty.garante'
    _description = 'Garantes de contratos'

    contacto = fields.Many2one('realty.contacto', 'Garante')
    contrato = fields.Many2one('realty.contrato', 'Contrato')
    nombre = fields.Char(related='contacto.nombre', string='Nombre', )
    dni = fields.Char(related='contacto.dni', string='DNI', )
