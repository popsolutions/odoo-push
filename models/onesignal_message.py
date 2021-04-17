from odoo import fields, models, api
from odoo.exceptions import Warning
import requests
import json
from _ssl import SSLError

class OnesignalMessage(models.Model):
    _name = 'onesignal.message'
    _rec_name = 'template_name'
    
    app_id = fields.Many2one('onesignal.credentials', 'App', required=True)
    template_name = fields.Char('Template Name')
    message_title = fields.Char('Message Title')
    message_content = fields.Text('Message Content')
    send_to_chrome = fields.Boolean('Send to Chrome', default=True, required=True)
    send_to_mozilla = fields.Boolean('Send to Mozilla', default=True)
    send_to_edge = fields.Boolean('Send to Edge', default=True)
    icon = fields.Char('Icon', required=True)
    launch_url = fields.Char('Launch URL')
    priority = fields.Selection([('10', 'High'),
                                 ('5', 'Normal')], default="5", help="""
                                 Priority
                                 """)
    time_to_live = fields.Integer('Time to live(days)', help="""
        The notification will expire if the device remains offline for these number of seconds. The default is 259,200 seconds (3 days).
    """, default=3)
    summary = fields.Char('Summary')
    
    @api.multi
    def raise_warning(self, warning_text):
        raise Warning(warning_text)

    @api.multi
    def get_key(self, var, priority):
        for key, val in var:
            if val.lower() == priority:
                return key
        
    @api.multi
    def get_app_data(self, app):
        header = {"Content-Type": "application/json; charset=utf-8",
          "Authorization": "Basic {}".format(app.apikey)}
        appln_id = app.app_id
        return {'header':header, 
                'app_id':appln_id}
    @api.multi
    def send_push_notification(self):
        self.ensure_one()
        if not self.app_id.is_active:
            raise_warning("{} is not active, Please activate it first.")
        appln_data = self.get_app_data(self.app_id)
        header = appln_data.get('header')
        var = self._fields['priority'].selection

        message_content = self.message_content
        message_content = message_content.encode('utf-8')

        message_title = self.message_title
        message_title = message_title.encode('utf-8')
        
        payload = {"app_id": "{}".format(appln_data.get('app_id')),
           "included_segments": ["All"],
           "contents": {"en": "{}".format(message_content)},
           "headings" :{"en": "{}".format(message_title)},
           "url": "{}".format(self.launch_url),
           "chrome_web_icon": "{}".format(self.icon),
           "ttl": self.time_to_live or 3,
           }
        if self.priority:
            priority = self.get_key(var,self.priority)
            payload.update({
                'priority':priority
                })
        if self.send_to_chrome or self.send_to_mozilla or self.send_to_edge:
            payload.update({
                'isAnyWeb': True
                })
        try:
            response = requests.post("https://onesignal.com/api/v1/notifications", headers=header, data=json.dumps(payload))
            if response.status_code == 200:
                resp = response.json()
                self.summary = "RECEIPIENTS : {}".format(resp.get('recipients'))
            else:
                self.summary = "Error : {}".format(response.text)
        except SSLError as ex:
            raise Warning("Oops, SSL Seems blocking the request.")
        except Exception as ex:
            raise Warning(ex)
            