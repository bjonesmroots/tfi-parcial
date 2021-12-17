# -*- coding: utf-8 -*-

from odoo import models, fields


class Contrato(models.Model):
    _name = 'realty.contrato'
    _description = 'Contratos de propiedades'

    propiedad_id = fields.Many2one('realty.propiedad', 'Propiedad')
    direccion_propiedad = fields.Text(related='propiedad_id.direccion', string='Propiedad', )
    fecha_inicio = fields.Date()
    fecha_fin = fields.Date()
    dia_vencimiento = fields.Integer()
    incremento = fields.Float()
    incremento_meses = fields.Integer()
    valor_inicial = fields.Float()
    inquilinos_ids = fields.One2many('realty.inquilino', 'contrato_id', string='Inquilinos', )
    garantes_ids = fields.One2many('realty.garante', 'contrato_id', string='Garantes', )
    alquileres_ids = fields.One2many('realty.alquiler', 'contrato_id', string='Alquileres', )
