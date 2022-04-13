{
    'name': "Manufacturing custom",
    'version': '15.0.1.0.0',
    'category': 'Manufcturing',
    'depends': ['mrp','stock'],
    'author': "Pravin Nayee",
    'license': 'LGPL-3',
    'summary': 'Tranning module',
    'description': """ Module for perform custumization on mrp module   """,
    'website': 'https://WWW.odoo.com',

    
    'data': [
        "wizard/mrp_workorder_views.xml",
    ],

    'installable': True,
    'auto_install': False,
    'application': True,

}
