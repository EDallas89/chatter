# -*- coding: utf-8 -*-
from odoo import http

# class Chatter(http.Controller):
#     @http.route('/chatter/chatter/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/chatter/chatter/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('chatter.listing', {
#             'root': '/chatter/chatter',
#             'objects': http.request.env['chatter.chatter'].search([]),
#         })

#     @http.route('/chatter/chatter/objects/<model("chatter.chatter"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('chatter.object', {
#             'object': obj
#         })