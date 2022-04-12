{
    'name': "sale appointment date",
    'version': '15.0.1.0.0',
    'category': 'Sales',
    'depends': ['sale_management','contacts','stock','product'],
    'author': "Pravin Nayee",
    'license': 'LGPL-3',
    'summary': 'Tranning module',
    'description': """ Module for perform odoo task """,
    'website': 'https://WWW.odoo.com',

    
    'data': [
        "views/stock_picking_views.xml",
        "views/res_partner_views.xml",
        "views/sale_order_views.xml",
        
    ],

    'installable': True,
    'auto_install': False,
    'application': True,

}
