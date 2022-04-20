{
    'name': 'Many2One Info Widget',
    'category': '',
    'summary': 'Many2One Info Widget',
    'author': "Center of Research and Development",
    'website': "https://crnd.pro",
    'license': 'LGPL-3',
    'version': '14.0.0.4.0',
    'depends': [
        'web',
    ],
    'data': [],
    'qweb': [
        'static/src/xml/popover_template.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'assets': {
        'web.assets_backend': [
            'crnd_web_m2o_info_widget/static/src/js/m2o_info_widget.js',
            'crnd_web_m2o_info_widget/static/src/js/form_renderer.js',
            'crnd_web_m2o_info_widget/static/src/scss/m2o_info_widget.scss'
        ]
    }
}
