$(document).ready(function () {
    $('.oe_website_sale').each(function () {
        var oe_website_sale = this;
        var $attr_to_reorder = $('#products_grid_before > form.js_attributes', oe_website_sale);
        var $categ_to_reorder = $('#products_grid_before > div#main_category', oe_website_sale);
        $categ_to_reorder.insertBefore($attr_to_reorder);
    });
});
