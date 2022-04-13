{
    'name': "website sale custom",
    'version': '15.0.1.0.0',
    'category':'ecommerce',
    'depends': ['stock' ],
    'author': "Pravin Nayee",
    'license': 'LGPL-3',
    'summary': 'Tranning module',
    'description': """ Module for add reorder button in webside sale order.""",
    'website': 'https://WWW.odoo.com',
    'data': [
        "views/sale_order_template.xml",
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
