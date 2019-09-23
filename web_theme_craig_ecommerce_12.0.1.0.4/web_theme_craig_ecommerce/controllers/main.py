# -*- coding: utf-8 -*-
# Part of Odoo Module Developed by 73lines
# See LICENSE file for full copyright and licensing details.

from odoo import http
from odoo.addons.website_sale.controllers.main import WebsiteSale


class WebsiteSaleRating(WebsiteSale):

    def get_rating_stat(self, product, context=None):
        rating_product = product.rating_get_stats(
            [('website_published', '=', True)])
        return rating_product

    @http.route()
    def shop(self, page=0, category=None, search='', ppg=False, **post):
        res = super(WebsiteSaleRating, self).shop(
            page=page, category=category, search=search, ppg=ppg, **post)
        res.qcontext.update({'get_rating_stat': self.get_rating_stat})
        return res
