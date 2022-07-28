# -*- coding: utf-8 -*-
# from odoo import http


# class AttsCustomPreferenceWizard(http.Controller):
#     @http.route('/atts_custom_preference_wizard/atts_custom_preference_wizard', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/atts_custom_preference_wizard/atts_custom_preference_wizard/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('atts_custom_preference_wizard.listing', {
#             'root': '/atts_custom_preference_wizard/atts_custom_preference_wizard',
#             'objects': http.request.env['atts_custom_preference_wizard.atts_custom_preference_wizard'].search([]),
#         })

#     @http.route('/atts_custom_preference_wizard/atts_custom_preference_wizard/objects/<model("atts_custom_preference_wizard.atts_custom_preference_wizard"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('atts_custom_preference_wizard.object', {
#             'object': obj
#         })
