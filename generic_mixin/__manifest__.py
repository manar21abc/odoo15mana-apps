{
    'name': "Generic Mixin",
    'summary': """
    Technical module with generic mixins, that may help to build other modules
    """,
    'author': "Center of Research and Development",
    'website': "https://crnd.pro",
    'category': 'Technical Settings',
    'version': '14.0.1.51.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'http_routing',
        'bus',
    ],
    'data': [],
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
    'assets': {
        'web.assets_backend': [
            'generic_mixin/static/src/js/refresh_view_mixin.js',
            'generic_mixin/static/src/js/web_client.js',
            'generic_mixin/static/src/js/abstract_view.js',
            'generic_mixin/static/src/js/abstract_controller.js',
            'generic_mixin/static/src/js/list_renderer.js',
            'generic_mixin/static/src/js/kanban_renderer.js',
            'generic_mixin/static/src/js/kanban_record.js'
        ]
    }
}
