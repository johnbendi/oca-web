# Copyright 2014 Therp BV (<http://therp.nl>).
# Copyright 2015 Leonardo Donelli @ MONKSoftware
# Copyright 2013 Marcel van der Boom <marcel@hsdev.com>
# Copyright 2016 - TODAY Serpent Consulting Services Pvt. Ltd.
#                            (<http://www.serpentcs.com>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "Show images in tree views via tooltip",
    "version": "15.0.1.0.0",
    "author": "Therp BV, "
    "MONK Software, "
    "Odoo Community Association (OCA), "
    "Serpent Consulting Services Pvt. Ltd.",
    "website": "https://github.com/OCA/web",
    "license": "AGPL-3",
    "category": "Web",
    "depends": ["web"],
    "data": [],
    "demo": [
        "demo/view_res_users.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "web_tree_image_tooltip/static/src/scss/common.scss",
            "web_tree_image_tooltip/static/src/js/tooltip.js",
        ],
    },
    "installable": True,
}
