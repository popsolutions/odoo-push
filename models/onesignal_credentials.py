from odoo import models, fields, api
from odoo.exceptions import Warning

class OnesignalCredentials(models.Model):
    _name = 'onesignal.credentials'
    
    name = fields.Char('App Name', help="Onesignal App name goes here", required=True)
    apikey = fields.Char('Api Key', help="Onsignal Api key", required=True)
    app_id = fields.Char('App ID', help="Onesignal App Id.", required=True)
    is_active = fields.Boolean('Is Active', help="Is Active")
    
    @api.multi
    def activate_app(self):
        self.ensure_one()
        if not self.is_active:
            #STEP 1 : CHECK IF BOOLEAN ACTIVE IN OTHER APP
            app_ids = self.search([('is_active','=',True)])
            if app_ids:
                raise Warning("Only one app can be active a time.")
            else:
                self.is_active = True
    
    @api.multi
    def deactivate_app(self):
        self.ensure_one()
        if self.is_active:
            self.is_active = False
        
