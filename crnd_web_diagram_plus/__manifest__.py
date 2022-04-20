{
    'name': 'CRnD Web Diagram Plus',
    'category': 'Technical Settings',
    'summary': """
        Odoo Web Diagram view by CRnD.
    """,
    'author': 'Center of Research and Development',
    'support': 'info@crnd.pro',
    'website': 'https://crnd.pro',
    'license': 'LGPL-3',
    'version': '14.0.0.4.1',
    'depends': [
        'web',
    ],
    'data': [],
    'qweb': [
        'static/src/xml/*.xml',
    ],
    'images': ['static/description/banner.png'],
    'installable': True,
    'auto_install': False,
    'assets': {
        'web.assets_backend': [
            'crnd_web_diagram_plus/static/src/js/vec2.js',
            'crnd_web_diagram_plus/static/src/js/graph.js',
            'crnd_web_diagram_plus/static/src/js/diagram_model.js',
            'crnd_web_diagram_plus/static/src/js/diagram_controller.js',
            'crnd_web_diagram_plus/static/src/js/diagram_renderer.js',
            'crnd_web_diagram_plus/static/src/js/diagram_view.js',
            'crnd_web_diagram_plus/static/src/js/view_registry.js'
        ]
    }
}
