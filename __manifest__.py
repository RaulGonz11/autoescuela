# -*- coding: utf-8 -*-
{
    'name': "autoescuela",

    'summary': "Módulo para la gestión integral de alumnos, profesores y exámenes de autoescuela",

    'description': """
Long description of module's purpose
    """,

    'icon':'/autoescuela/static/description/autoescuela.png',

    'author': "Tania Garcia", # Nombre del creador [cite: 1027]
    'website': "https://www.tuautoescuela.com", # URL opcional [cite: 1028]
    'category': 'Productivity', # Categoría del módulo [cite: 1029, 1096]
    'version': '0.1', # Versión inicial


    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'data/autoescuela_sequence.xml',
        'security/autoescuela_security.xml',
        'security/ir.model.access.csv',
        'views/autoescuela_alumno_view.xml',
        'views/autoescuela_autoescuela_view.xml',
        'views/autoescuela_profesor_view.xml',
        'views/autoescuela_examen_view.xml',
        'views/autoescuela_menus.xml',
        'reports/autoescuela_alumno_report.xml',
        'reports/autoescuela_autoescuela_report.xml',
        'reports/autoescuela_examen_report.xml', 
        'reports/autoescuela_profesor_report.xml',
        'reports/autoescuela_alumno_report_html.xml',
        'reports/autoescuela_autoescuela_report_html.xml',
        'reports/autoescuela_profesor_report_html.xml',
        'reports/autoescuela_examen_report_html.xml',
        # 'security/autoescuela_security.xml',
        # 'security/ir.model.access.csv',
        # 'views/autoescuela_alumno_view.xml',
        # 'views/autoescuela_profesor_view.xml',
        # 'views/autoescuela_examen_view.xml',
        # 'views/autoescuela_menus.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    # Es obligatorio marcarlo como True para que aparezca en el buscador de aplicaciones [cite: 4646, 5175]
    'application': True,
}

