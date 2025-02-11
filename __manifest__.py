{
'name': 'Servicio de Mantenimiento',
'version': '1.0',
'author': 'Héctor Martín Ortega',
'category': 'Custom',
'summary': 'Gestión de Mantenimiento de Productos',
'depends': ['base', 'garantias'],
'data': [
'security/ir.model.access.csv',
'views/servicio_mantenimiento_views.xml',
],
'icon': '/garantias/static/description/icon55.png',
'installable': True,
'application': True,
}