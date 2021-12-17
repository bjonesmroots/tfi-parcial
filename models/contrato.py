# -*- coding: utf-8 -*-

from odoo import models, fields


class Contrato(models.Model):
    _name = 'realty.contrato'
    _description = 'Contratos de propiedades'

    propiedad = fields.Many2one('realty.propiedad', 'Propiedad')
    direccion_propiedad = fields.Text(related='propiedad.direccion', string='Propiedad', )
    fecha_inicio = fields.Date()
    fecha_fin = fields.Date()
    dia_vencimiento = fields.Integer()
    incremento = fields.Float()
    incremento_meses = fields.Integer()
    valor_inicial = fields.Float()
    interes_diario = fields.Float()
    inquilinos = fields.One2many('realty.inquilino', 'contrato', string='Inquilinos', )
    garantes = fields.One2many('realty.garante', 'contrato', string='Garantes', )
    alquileres = fields.One2many('realty.alquiler', 'contrato', string='Alquileres', )
