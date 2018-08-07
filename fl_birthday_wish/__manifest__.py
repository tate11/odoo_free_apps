# -*- coding: utf-8 -*-

{
    'name': 'Birthday Wishes',
    'version': '11.0.1.0.0',
    'category': 'Contacts',
    'summary': 'Birthday Wishes for Employee, Customer',
    'description': """
        This module send email notification to wish birthday
        * Employee
        * Customer
        * Partner
    """,
    'sequence': 1,
    'author': 'Futurelens',
    'website': 'http://thefuturelens.com',
    'depends': ['base', 'hr', 'contacts'],
    'data': [
        'data/birthday_wish_cron.xml',
        'data/mail_template_birthday_data.xml',
        'views/res_partner_view.xml',
    ],
    'qweb': [],
    'css': [],
    'js': [],
    'images': [
        'static/description/birthday_wishes_banner.png',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3'
}
