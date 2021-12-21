# -*- coding: utf-8 -*-

from odoo import models, fields


class Propiedad(models.Model):
    _name = 'realty.propiedad'
    _description = 'Propiedad de una inmobiliaria registrada en el sistema'

    inmobiliaria = fields.Many2one('realty.inmobiliaria', 'Inmobiliaria')
    nombre = fields.Char()
    direccion = fields.Text()
    propietarios = fields.One2many('realty.propietario', 'propiedad', string='Propietarios', )
    contratos = fields.One2many('realty.contrato', 'propiedad', string='Contratos', )

    def name_get(self):
        result = []
        for record in self:
            result.append((record.id, record.direccion))
        return result
