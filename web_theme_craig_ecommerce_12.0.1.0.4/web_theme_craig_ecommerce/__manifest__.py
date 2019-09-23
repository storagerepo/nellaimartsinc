# -*- coding: utf-8 -*-
# Part of Odoo Module Developed by 73lines
# See LICENSE file for full copyright and licensing details.

{
    'name': 'Craig Theme Ecommerce',
    'description': 'Craig Theme is theme developed by 73Lines '
                   'Development Team consist of 35+ snippets '
                   'to build a beautiful website with 8 '
                   'color variations, 12 font options, 2 '
                   'Layouts and 8 Patterns.',
    'category': 'Website',
    'version': '12.0.1.0.4',
    'summary': 'Multi Purpose Ecommerce,Responsive '
               'and Fully Customizable Odoo Theme',
    'author': '73Lines',
    'website': 'https://www.73lines.com',
    'depends': [

        # Default Modules

        'website',
        'web_theme_craig',
        'website_mass_mailing',
        'website_blog',
        'website_crm',
        'website_sale',
        'website_sale_comparison',
        'theme_default',
        'website_theme_install',
        # 73lines Depend Modules

        # Don't forget to see README file in order to how to install
        # In order to install complete theme, uncomment the following.
        # Dependent modules are supplied in a zip file along with the theme,
        # if you have not received it,please contact us at enquiry@73lines.com
        # with proof of your purchase.
        ###############################################################

        'website_header_business_73lines',
        'carousel_slider_73lines',
        'snippet_blog_carousel_73lines',
        'snippet_product_brand_carousel_73lines',
        'snippet_product_carousel_73lines',
        'snippet_product_category_carousel_73lines',
        'snippet_recently_viewed_product_carousel_73lines',
        'website_header_layout_73lines',
        'website_language_flag_73lines',
        'website_product_categ_menu_and_banner_73lines',
        'website_product_misc_options_73lines',
        'website_product_page_layout_73lines',
        'website_product_ribbon_73lines',
        'website_product_share_options_73lines',
        'website_mega_menu_73lines',
        'website_product_quick_view_73lines',
        'website_product_back_image_on_hover',
        'snippet_boxed_73lines',
        'icon_fonts_73lines',
        'google_dynamic_font',

        ###############################################################

    ],
    'data': [
        'views/assets.xml',
        'views/homepage.xml',
        'views/mid_header_template.xml',
        'views/s_blog_carousel.xml',
        'views/product_carousel.xml',
        'views/products_template.xml',
        'views/product_collapse_categories_template.xml',
        'views/shop_single_product_template.xml',
        'views/footer_template.xml',
        'views/snippets/side_banner.xml',
        'views/snippets/s_testimonial.xml',
        'views/snippets/s_banner_3_image.xml',
        'views/snippets/main_banner.xml',
        'views/snippets/tab_carousel_side_banner.xml',
        'views/snippets/brand_carousel_and_testimonials.xml',
    ],
    'demo': [
        'data/brand_demo.xml',
    ],
    'images': [
        'static/description/craig-ecommerce-banner.png',
    ],
    'price': 50,
    'application': True,
    'license': 'OPL-1',
    'currency': 'EUR',
    'live_test_url': 'https://www.73lines.com/r/1EH'
}
