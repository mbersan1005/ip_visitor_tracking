{
'name': 'Ip Visitor Tracking',
'version': '1.0',
'summary': 'Integración con la API de Ipgeolocation',
'description': 'Obtención de datos de geolocalización en tiempo real.',
'author': 'Miguel Ángel Bernal Sánchez',
'category': 'Website',
'depends': ['base'],
'data': [
    'security/ir.model.access.csv',
    'views/traking_view.xml',
],
'icon': ['/ip_visitor_tracking/static/description/icon58.png'],
'installable': True,
'application': True,
'license': 'LGPL-3',
}