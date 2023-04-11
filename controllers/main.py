from odoo import http
from odoo.http import request, route

class T4Web(http.Controller):
    @http.route(["/"], type="http", auth="public" , website=True)
    def show_playground(self):
        return request.render("t4_web.dmm")

    @http.route(["/my/setting"], type="http", auth="public" , website=True)
    def setting(self):
        return request.render("t4_web.setting")

    @http.route(["/my/securityy"], type="http", auth="public" , website=True)
    def security(self):
        return request.render("t4_web.portal_my_securityy")
