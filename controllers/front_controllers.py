# -*- coding: utf-8 -*-
import datetime

from odoo import http
from odoo.http import request
from datetime import date
from ..models.mercadopagoAPI import MercadoPagoAPI


class realty(http.Controller):
    @http.route('/realty/suscribir', website=True, auth='public')
    def realty_suscribir(self, **kw):
        return request.render('realty.suscribir_page', {
            'planes': http.request.env['realty.plan'].search([]),
            'inmobiliaria': http.request.env['realty.inmobiliaria'].search([("id", "=", 2)])
        })

    @http.route('/realty/plan/<int:plan_id>', website=True, auth='public')
    def realty_plan(self, plan_id, **kw):
        return request.render('realty.plan_page', {
            'plan': http.request.env['realty.plan'].search([("id", "=", plan_id)]),
            'inmobiliaria': http.request.env['realty.inmobiliaria'].search([("id", "=", 2)])
        })

    @http.route('/realty/guardarSuscripcion', type="http", website=True, auth='public')
    def realty_guardar_suscripcion(self, **kw):
        tarjeta_val ={
            'numero': kw.get('tarjeta_numero'),
            'nombre': kw.get('tarjeta_nombre'),
            'exp': kw.get('tarjeta_exp'),
            'csv': kw.get('tarjeta_security_code')
        }
        if MercadoPagoAPI.validarTarjeta(tarjeta_val):
            suscripcion_val = {
                'plan_id': kw.get('plan_id'),
                'inmobiliaria_id': kw.get('inmobiliaria_id'),
                'fecha_ultimo_cobro': date.isoformat(date.today()),
                'id_mercadopago': MercadoPagoAPI.procesarSuscripcion(tarjeta_val)
            }
            http.request.env['realty.suscripcion'].sudo().create(suscripcion_val)
            return request.render('realty.thanks_page', {
                'plan': http.request.env['realty.plan'].search([("id", "=", kw.get('plan_id'))]),
                'inmobiliaria': http.request.env['realty.inmobiliaria'].search([("id", "=", 2)])
            })
        else:
            return request.render('realty.error_page', {
                'plan': http.request.env['realty.plan'].search([("id", "=", kw.get('plan_id'))]),
                'inmobiliaria': http.request.env['realty.inmobiliaria'].search([("id", "=", 2)])
            })

    @http.route('/realty/cobrar', website=True, auth='public')
    def realty_cobrar(self, **kw):
        return request.render('realty.cobrar_alquiler_page', {
            'alquiler': http.request.env['realty.alquiler'].search([("id", "=", kw.get('id'))]),
        })
