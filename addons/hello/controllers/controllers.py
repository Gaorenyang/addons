# -*- coding: utf-8 -*-
from odoo import http

# class Hello(http.Controller):
#     @http.route('/hello/hello/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hello/hello/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hello.listing', {
#             'root': '/hello/hello',
#             'objects': http.request.env['hello.hello'].search([]),
#         })

#     @http.route('/hello/hello/objects/<model("hello.hello"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hello.object', {
#             'object': obj
#         })