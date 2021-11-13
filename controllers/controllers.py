# -*- coding: utf-8 -*-
# from odoo import http


# class .\odoo\addons\realty\(http.Controller):
#     @http.route('/.\odoo\addons\realty\/.\odoo\addons\realty\/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/.\odoo\addons\realty\/.\odoo\addons\realty\/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('.\odoo\addons\realty\.listing', {
#             'root': '/.\odoo\addons\realty\/.\odoo\addons\realty\',
#             'objects': http.request.env['.\odoo\addons\realty\..\odoo\addons\realty\'].search([]),
#         })

#     @http.route('/.\odoo\addons\realty\/.\odoo\addons\realty\/objects/<model(".\odoo\addons\realty\..\odoo\addons\realty\"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('.\odoo\addons\realty\.object', {
#             'object': obj
#         })
