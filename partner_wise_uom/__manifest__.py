{
    'name': "Partner wise uom",
    'version': '15.0.1.0.0',
    'category': 'Sales',
    'depends': ['sale_stock','sale_management','stock','contacts'],
    'author': "Pravin Nayee",
    'license': 'LGPL-3',
    'summary': 'Tranning module',
    'description': """ Module for show partner wise product unit of mesure in sale order and invoice  """,
    'website': 'https://WWW.odoo.com',

    
    'data': [
        "security/ir.model.access.csv",
        "views/partner_wise_uom_views.xml",
    ],

    'installable': True,
    'auto_install': False,
    'application': True,

}
