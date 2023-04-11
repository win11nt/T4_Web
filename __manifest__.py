# -*- coding: utf-8 -*-
{
    "name": "T4 Web",
    "summary": """
        Frontend lam""",
    "description": """
        Ok Luon
    """,
    "author": "T4Tek Team",
    "website": "https://t4tek.co/",
    "category": "T4/Website",
    "version": "16.0.1.0.0",
    "depends": ["t4", "website"],
    "data": [
        "views/begin/header_after_login.xml",
        "views/begin/footer.xml",
        "views/begin/header.xml",
        "views/dmm.xml",
        "views/setting/setting.xml",
        "views/security.xml",
    ],
    "license": "LGPL-3",
    "assets":{
        "t4_web.header":[
            "t4_web/static/src/js/jquery.js",
            "t4_web/static/src/js/nicepage.js",
            "t4_web/static/src/css/nicepage.css",
            "t4_web/static/src/css/Home.css",
        ],
        "t4_web.header_after_login":[
            "t4_web/static/src/js/jquery.js",
            "t4_web/static/src/js/nicepage-after-login.js",
            "t4_web/static/src/css/nicepage-after-login.css",
            # "t4_web/static/src/css/Setting.css"
        ],
        "t4_web.footer":[
            "t4_web/static/src/js/jquery.js",
            "t4_web/static/src/js/nicepage.js",
            "t4_web/static/src/css/nicepage.css",
        ],
        "t4_web.assets_home":[
            "t4_web/static/src/js/jquery.js",''
            "t4_web/static/src/js/nicepage.js",
            "t4_web/static/src/css/nicepage.css",
        ],
        "t4_web.assets_setting":[
            "t4_web/static/src/css/jquery.js",
            "t4_web/static/src/css/setting.css",
            "t4_web/static/src/css/nicepage.css",
            "t4_web/static/src/css/nicepage.js",
            "t4_web/static/src/js/setting.js",

        ],
        "t4_web.css_scroll":[
            "t4_web/static/src/css/scroll.css"
        ],
        "t4_web.padding":[
            "t4_web/static/src/css/padding.css"
        ],
         "t4_web.css_input":[
            "t4_web/static/src/css/input.css"
        ],
    },
}
