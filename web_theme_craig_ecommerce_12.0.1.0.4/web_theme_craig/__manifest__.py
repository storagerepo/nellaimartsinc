# -*- coding: utf-8 -*-
# Part of Odoo Module Developed by 73lines
{
    'name': 'Theme Craig',
    'description': 'Theme Craig',
    'category': 'Website',
    'version': '12.0.1.0.0',
    'author': '73Lines',
    'website': 'https://www.73lines.com',
    'data': [
        # Snippets
        'views/snippets/s_our_service.xml',
        'views/snippets/s_about_us.xml',
        'views/snippets/s_testimonial_faq.xml',
        'views/snippets/s_our_team.xml',
        'views/snippets/s_service.xml',
        'views/snippets/s_dark_counter.xml',
        'views/snippets/s_we_best.xml',
        'views/snippets/s_blog_carousel.xml',
        'views/snippets/s_title_subtitle.xml',
        'views/snippets/s_title_subtitle_text.xml',

        # Templates
        'views/assets.xml',
        'views/mid_header_template.xml',
        'views/404_page_template.xml',
        'views/contact_us_page.xml',
        'views/blog_page.xml',
        'views/aboutus_page.xml',
        'views/modern-services.xml',
        'views/homepage.xml',
        'views/brand_page.xml',
        'views/testimonial_page.xml',
        'views/footer_template.xml',
    ],
    'demo': [
        'data/menu_data.xml',
        'data/blog_post_demo.xml',
    ],
    'depends': [
        # Default Modules
        'website',
        'website_mass_mailing',
        'website_blog',
        'website_crm',
        'theme_default',
        'website_theme_install',
        # 73lines Depend Modules
        # Don't forget to see README file in order to how to install
        # In order to install complete theme, uncomment the following.
        # Dependent modules are supplied along with the theme,
        # if you have not received it,please contact us at
        # enquiry@73lines.com with proof of your purchase.
        ###############################################################
        'carousel_slider_73lines',
        'snippet_boxed_73lines',
        'snippet_blog_carousel_73lines',
        'website_header_business_73lines',
        'website_mega_menu_73lines',
        'icon_fonts_73lines',
        'website_language_flag_73lines',
        ###############################################################
    ],
    'images': [
        'static/description/craig-banner.png',
    ],
    'qweb': ['static/xml/dashboard_ext.xml'],
    'application': True,
    'price': 150,
    'currency': 'EUR',
    'license': 'OPL-1',
    'live_test_url': 'https://www.73lines.com/r/3k3'
}
