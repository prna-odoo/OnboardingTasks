{
    'name': "Credit limit",
    'version': '15.0.1.0.0',
    'category': 'Sale',
    'depends': ['sale_management','sale_stock','stock'],
    'author': "Pravin Nayee",
    'license': 'LGPL-3',
    'summary': 'Tranning module',
    'description': """ Module for set credit limit on customer   """,
    'website': 'https://WWW.odoo.com',

    
    'data': [
        "views/credit_limit_views.xml",
    ],

    'installable': True,
    'auto_install': False,
    'application': True,

}
