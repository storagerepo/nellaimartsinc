# -*- coding: utf-8 -*-
# Copyright (C) 2017-Today  Technaureus Info Solutions(<http://technaureus.com/>).

{
    'name': 'Pos Shortcut Access',
    'version': '12.0.0.2',
    'sequence':1,
    'category': 'Point of Sale',
    'author': 'Technaureus Info Solutions Pvt. Ltd.',
    'website': 'http://www.technaureus.com/',
    'summary': 'Pos shortcut allows us to access point of sale with keyboard shortcuts.',
    'description': """
=======================
Pos shortcut allows us to access point of sale with keyboard shortcuts.
""",
    'depends': ['point_of_sale'],
    'price': 35,
    'currency': 'EUR',
    'license': 'Other proprietary',
    'data': [
        'views/views.xml',
        'views/templates.xml'
    ],
    'qweb': [
        'static/src/xml/pos.xml',
    ],
    'images': ['images/main_screenshot.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
