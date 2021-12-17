# -*- coding: utf-8 -*-

from odoo import models, fields, http
from odoo.http import request
from datetime import date


class Alquiler(models.Model):
    _name = 'realty.alquiler'
    _description = 'Alquiler de un contrato registrado en el sistema'

    contrato_id = fields.Many2one('realty.contrato', 'Contrato')
    fecha = fields.Date()
    fecha_vencimiento = fields.Date()
    valor = fields.Float()
    estado = fields.Char(string='Estado', compute='_compute_estado')
    recibos_ids = fields.One2many('realty.recibo', 'alquiler_id', string='Recibos', )

    def _compute_estado(self):
        for record in self:
            if date.today() > record.fecha_vencimiento:
                if len(record.recibos_ids) > 0:
                    record.estado = 'Pagado'
                else:
                    record.estado = 'Vencido'
            elif record.fecha < date.today() < record.fecha_vencimiento:
                record.estado = 'Vigente'
            elif date.today() < record.fecha:
                record.estado = 'Futuro'

    def cobrarClickEvent(self):
        return {
            'type': 'ir.actions.act_url',
            'url': 'http://localhost:8069/realty/cobrar',
            'target': 'new',
        }
