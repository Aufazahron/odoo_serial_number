
{
    'name': 'Custom Serial Number for Manufacturing Orders',
    'version': '1.0',
    'summary': 'Generate custom serial numbers for specific products in Manufacturing Orders',
    'description': 'Automatically generates serial numbers with specific prefixes (e.g., CAxxxx or CBxxxx) based on the product type in Manufacturing Orders.',
    'author': 'Your Name',
    'category': 'Manufacturing',
    'depends': ['mrp', 'stock'],
    'data': [
        'views/mrp_production_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
