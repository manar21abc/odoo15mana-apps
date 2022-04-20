{
    'name':
    'Website Service Desk',
    'category':
    'Service Desk',
    'summary':
    'Website UI for Service Desk',
    'author':
    "Center of Research and Development",
    'website':
    "https://crnd.pro",
    'license':
    'LGPL-3',
    'version':
    '14.0.1.75.0',
    'depends': [
        'mail',
        'website',
        'website_mail',
        'crnd_service_desk',
    ],
    'data': [
        'security/security.xml',
        'templates/templates.xml',
        'templates/templates_request_page.xml',
        'templates/templates_request_new_page.xml',
        'views/request_type_view.xml',
        'views/request_stage_route.xml',
        'views/request_category_view.xml',
        'views/request_kind.xml',
        'views/request_request.xml',
        'views/res_config_settings.xml',
        'data/website_data.xml',
        'data/request_type_incident.xml',
    ],
    'demo': [
        'demo/demo_res_users.xml',
        'demo/demo_category.xml',
        'demo/request_kind.xml',
        'demo/demo_generic_type.xml',
        'demo/demo_upgrade_type.xml',
        'demo/demo_request_type_seq.xml',
        'demo/demo_bug_report_type.xml',
    ],
    'qweb': [
        'static/src/xml/templates.xml',
    ],
    'images': ['static/description/banner.gif'],
    'installable':
    True,
    'auto_install':
    False,
    'assets': {
        'website.assets_frontend': [
            'crnd_wsd/static/lib/trumbowyg/dist/trumbowyg.min.js',
            'crnd_wsd/static/lib/trumbowyg/dist/langs/ua.min.js',
            'crnd_wsd/static/lib/trumbowyg/dist/langs/ru.min.js',
            'crnd_wsd/static/lib/trumbowyg/dist/plugins/table/trumbowyg.table.min.js',
            'crnd_wsd/static/lib/trumbowyg/dist/plugins/colors/trumbowyg.colors.min.js',
            'crnd_wsd/static/lib/trumbowyg/dist/ui/trumbowyg.min.css',
            'crnd_wsd/static/lib/trumbowyg/dist/plugins/table/ui/trumbowyg.table.min.css',
            'crnd_wsd/static/lib/trumbowyg/dist/plugins/colors/ui/trumbowyg.colors.min.css',
            'crnd_wsd/static/src/js/trumbowyg.upload-file.js',
            'crnd_wsd/static/src/js/trumbowyg.js',
            'crnd_wsd/static/src/js/blockui.js',
            'crnd_wsd/static/src/js/request_discussion.js',
            'crnd_wsd/static/src/js/request_new.js',
            'crnd_wsd/static/src/js/request_new_step.js',
            'crnd_wsd/static/src/js/request_actions.js',
            'crnd_wsd/static/src/js/enable_popovers.js',
            'crnd_wsd/static/src/js/widgets.js',
            'crnd_wsd/static/src/scss/request.scss',
            'crnd_wsd/static/src/scss/blockui_spin.css'
        ],
        'web.assets_common': [
            'crnd_wsd/static/src/js/tours/request_mail_login_portal.js'
            'crnd_wsd/static/src/js/tours/request_action_no_actions.js'
            'crnd_wsd/static/src/js/tours/request_action_actions.js'
            'crnd_wsd/static/src/js/tours/request_action_actions_redirect.js'
            'crnd_wsd/static/src/js/tours/request_base.js'
            'crnd_wsd/static/src/js/tours/request_new.js'
            'crnd_wsd/static/src/js/tours/request_new_default_text.js'
            'crnd_wsd/static/src/js/tours/request_public_user.js'
            'crnd_wsd/static/src/js/tours/request_public_user_redirect.js'
            'crnd_wsd/static/src/js/tours/request_public_user_create_req.js'
            'crnd_wsd/static/src/js/tours/request_filter_kind.js'
        ]
    }
}
