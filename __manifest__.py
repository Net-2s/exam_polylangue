# -*- coding: utf-8 -*-
{
    'name': "Polylanguee Exam",
    'summary': """""",
    'description': """""",
    'author': "Loic DNJOMOU",
    'website': "https://digitalexpertize.com",
    'category': 'Uncategorized',
    'version': '16.0.1',
    'depends': ['base', 'account', 'gestion_formation','edof_data'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/inscription.xml',
        'views/session.xml',
        'views/folder.xml',
        'views/res_user_view.xml',
        'views/res_config_settings_views.xml',
        'views/product_view.xml',
        'views/res_branch_view.xml',
        'data/convocation_mail_template_cpf.xml',
        'data/convocation_mail_template_edof.xml',
        'data/mail_template_data.xml',
        'data/product_template.xml'
    ],
    "license": "OPL-1",
    'installable': True,
    'application': True,
    'auto_install': False,
}
