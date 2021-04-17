{
    'name': 'Odoo Push Notification Using One Signal',
    'version': '12.0.0',
    'category': 'Push Notifications',
    'summary': 'This module adds one signal push notification functionality for odoo website. odoo push notifications Odoo Push Notification push notification module push notification app',
    'description': '''
Odoo Push Notification Using One Signal
=======================================
This module adds one signal push notification functionality for odoo website
<keywords>
odoo push notifications
push notifications
notifications
Odoo Push Notification
push notification module
push notification app
    ''',
    'author': 'Pragmatic TechSoft Pvt Ltd.',
    'website': 'www.pragtech.co.in',
    'depends': ['website'],
    'data': [
        'security/user_groups.xml',
        'security/ir.model.access.csv',
        'views/onesignal_credentials_view.xml',
        'views/onesignal_message_view.xml',
        'views/template_assets.xml'
    ],
    'price': 90.00,
    'currency': 'USD',
    'license': 'OPL-1',
    'images': ['images/Animated-Push-Notification.gif'],
    'live_test_url': 'http://www.pragtech.co.in/company/proposal-form.html?id=103&name=push-notification',
    'installable': True,
    'application': True,
    'auto_install': False,
}
