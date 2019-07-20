from odoo import http

class MyModule(http.Controller):
    @http.route('/gestion_formation/gestion_formation/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/gestion_formation/gestion_formation/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('gestion_formation.listing', {
            'root': '/gestion_formation/gestion_formation',
            'objects': http.request.env['gestion_formation.gestion_formation'].search([]),
        })

    @http.route('/gestion_formation/gestion_formation/objects/<model("gestion_formation.gestion_formation"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('gestion_formation.object', {
            'object': obj
        })