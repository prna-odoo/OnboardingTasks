{
    'name': "Project task separation",
    'version': '15.0.1.0.0',
    'category': 'Productivity',
    'depends': ['project'],
    'author': "Pravin Nayee",
    'license': 'LGPL-3',
    'summary': 'Tranning module',
    'description': """ Module for separation of main task and subtasks """,
    'website': 'https://WWW.odoo.com',

    
    'data': [
        "views/project_task_separation_views.xml",
    ],

    'installable': True,
    'auto_install': False,
    'application': True,

}
