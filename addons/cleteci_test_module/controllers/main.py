from odoo import http
from odoo.http import request

class CleteciController(http.Controller):
    @http.route('/cleteci/api', auth='public', type='json', methods=['GET'], csrf=False)
    def get_cleteci(self, **kwargs):
        records = request.env['cleteci.model'].search([])
        return [{
            'id': rec.id,
            'name': rec.name,
            'description': rec.description
        } for rec in records]