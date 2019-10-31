# -*- coding: utf-8 -*-
{
    'name': "custom-module",

    'summary': """Module to be used to custom changes in odoo""",

    'description': """Deemsys changes will go into this module""",

    'author': "Deemsys",
    'website': "http://www.deemsysinc.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Odoo Source',
    'version': '0.3',

    # any module necessary for this one to work correctly
    'depends': ['base','website_sale'],

    # always loaded
    'data': [],
    # only loaded in demonstration mode
    'demo': [],
    'installable': True,
    'auto_install': False,
}