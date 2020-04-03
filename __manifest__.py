# -*- coding: utf-8 -*-
{
    'name': "Chatter for Bank Statements",
    'summary': """
        Añade las funciones de mensajería, planificación de actividades, 
        archivos adjuntos y seguidores en los extractos bancarios.""",
    'author': "Inma Sánchez",
    'website': "https://github.com/EDallas89",
    'category': 'Gestión de facturación',
    'version': '12.0',
    'depends': ['base', 'account'],
    'data': [
        'views/views.xml',
    ],
    'installable': True,
    'application': True,
}