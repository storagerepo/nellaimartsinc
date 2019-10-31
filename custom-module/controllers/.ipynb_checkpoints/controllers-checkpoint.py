
from odoo.addons.website_sale.controllers.main import WebsiteSale
from odoo.addons.portal.controllers.portal import CustomerPortal
from odoo.addons.website_sale_wishlist.controllers.main import WebsiteSaleWishlist
from odoo import http
from odoo.http import request


class SaleController(WebsiteSale):
    @http.route(auth='user')
    def checkout(self, **post):
         #the user is logged in to checkout
         return super(SaleController, self).checkout(**post)
    
class CustomDeemPortal(CustomerPortal):
    @http.route(auth='user')
    def account(self, redirect=None, **post):
        
        CustomerPortal.MANDATORY_BILLING_FIELDS = ["name", "phone", "email", "street", "city", "country_id","zipcode", "state_id"]
        CustomerPortal.OPTIONAL_BILLING_FIELDS = ["vat", "company_name"]
    
        return CustomerPortal.account(self,redirect=None,**post)
    
class WebsiteWishlistCustom(WebsiteSaleWishlist):
    @http.route(['/shop/wishlist'], type='http', auth="public", website=True)
    def get_wishlist(self, count=False, **kw):
        values = request.env['product.wishlist'].with_context(display_default_code=False).current()
        if count:
            return request.make_response(json.dumps(values.mapped('product_id').ids))

        if not len(values):
             return request.render("website_sale_wishlist.product_wishlist", dict(wishes=[]))

        return request.render("website_sale_wishlist.product_wishlist", dict(wishes=values))
        