# -*- coding: utf-8 -*-
{
    'name': "AttentiveScience Custom Preference Wizard",

    'summary': """
        customizing the Preference wizard view""",

    'description': """
        making the user preference view simple, by removing the "developer api" and re-position "change password" button
    """,

    'author': "Philemon Acheapong",
    'website': "https://www.attentivescience.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tool',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
