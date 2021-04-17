from odoo.http import Controller, request
from odoo import http


class ActiveAppCtrl(Controller):
    
    @http.route('/check_active_app', auth="public", csrf=False, type="http")
    def check_active_app(self):
        '''
            This method will return active app id else will return 0
            @params : None
            @returns : Appid else 0
        '''
        appln_id = request.env['onesignal.credentials'].sudo().search([('is_active','=',True)])
        if appln_id:
            return appln_id.app_id
        else:
            return "0"