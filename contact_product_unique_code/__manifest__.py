{
    'name': "Contect & prodct unique code",
    'version': '15.0.1.0.0',
    'category':'Services',
    'depends': ['contacts','account','stock'],
    'author': "Pravin Nayee",
    'license': 'LGPL-3',
    'summary': 'Tranning module',
    'description': """ Module for edit contact module and add unique code for customer and vendor also add new sequences for product  """,
    'website': 'https://WWW.odoo.com',

    
    'data': [
        "data/ir_sequence_data.xml",
        "views/contact_view.xml",
        "views/product_custom_views.xml",
        
    ],

    'installable': True,
    'auto_install': False,
    'application': True,

}
