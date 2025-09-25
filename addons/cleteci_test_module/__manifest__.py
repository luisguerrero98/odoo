{
    'name': 'Cleteci Module',
    'version': '1.0',
    'summary': 'Test module for Odoo 19.0',
    'author': 'Cleteci',
    'category': 'Test',
    'depends': ['base'],
    'data': [
        'data/cleteci_model_data.xml',

        'security/ir.model.access.csv',
        
        'views/cleteci_model_view.xml',
        'views/cleteci_menu.xml',
    ],
    'installable': True,
    'application': True,
}