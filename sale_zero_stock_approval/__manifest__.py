{
    'name': "Sale zero stock approval",
    'version': '15.0.1.0.0',
    'category': 'Sale',
    'depends': ['sale_management','sale_stock','stock'],
    'author': "Pravin Nayee",
    'license': 'LGPL-3',
    'summary': 'Tranning module',
    'description': """ Module for approval of zero stock fro selected client""",
    'website': 'https://WWW.odoo.com',

    
    'data': [
        "security/security.xml",
        "security/ir.model.access.csv",
        "views/sale_approval_views.xml",
    ],

    'installable': True,
    'auto_install': False,
    'application': True,

}
