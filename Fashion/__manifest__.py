# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Fashion',
    'version': '1.1',
    'category': 'Design',
    'sequence': 75,
    'summary': 'Centralize style information',
    'description': "",
    'website': 'https://www.flixalogix.com',
    'images': [
    ],
    'depends': [
        'base_setup',
        'sale',
    ],
    'data': [

        'views/res_config_settings_views.xml',
    ],
    'demo': [
        'data/hr_demo.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'qweb': [],
}
