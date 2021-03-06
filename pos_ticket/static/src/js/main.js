odoo.define('pos_custom_model', function (require) {
    var core = require('web.core');
    var rpc = require('web.rpc');
    var module = require('point_of_sale.models');
    var PosBaseWidget = require('point_of_sale.BaseWidget');
    var posDb = require('point_of_sale.DB');
    var screenWidget=require('point_of_sale.screens');
    var models = module.PosModel.prototype.models;
    var _t = core._t;
    for (var i = 0; i < models.length; i++) {
        var model = models[i];
        if (model.model === 'res.company') {
            model.fields.push('street');
            model.fields.push('city');
            model.fields.push('state_id');
            model.fields.push('country_id');
        }
    }
    //To remove $ in subtotal   
    PosBaseWidgetCustom = PosBaseWidget.include({
        format_currency_custom: function (amount, precision) {

            amount = this.format_currency(amount, precision);
            amount = amount.replace(' ', '');
            return amount;
        }
    })
    
    screenWidgetCustom=screenWidget.ClientListScreenWidget.include({
        save_client_details: function(partner) {
        var self = this;
        
        var fields = {};
        this.$('.client-details-contents .detail').each(function(idx,el){
            fields[el.name] = el.value || false;
        });

        if (!fields.name && !fields.email && !fields.phone) {
            this.gui.show_popup('error',_t('Customer Name or Email ID or Phone Number is required'));
            return;
        }
        if(fields.name && fields.lastName){
            fields.name+=" "+fields.lastName;
        }
        if(!fields.name){
            fields.name="Unknown"
        }
        
        if (this.uploaded_picture) {
            fields.image = this.uploaded_picture;
        }
        fields.mobile       = fields.phone;
        fields.id           = partner.id || false;
        fields.country_id   = fields.country_id || false;

        if (fields.property_product_pricelist) {
            fields.property_product_pricelist = parseInt(fields.property_product_pricelist, 10);
        } else {
            fields.property_product_pricelist = false;
        }
        var contents = this.$(".client-details-contents");
        contents.off("click", ".button.save");


        rpc.query({
                model: 'res.partner',
                method: 'create_from_ui',
                args: [fields],
            })
            .then(function(partner_id){
                self.saved_client_details(partner_id);
            },function(err,ev){
                ev.preventDefault();
                var error_body = _t('Your Internet connection is probably down.');
                if (err.data) {
                    var except = err.data;
                    error_body = except.arguments && except.arguments[0] || except.message || error_body;
                }
                self.gui.show_popup('error',{
                    'title': _t('Error: Could not Save Changes'),
                    'body': error_body,
                });
                contents.on('click','.button.save',function(){ self.save_client_details(partner); });
            });
    },
    edit_client_details: function(partner) {
        partner_name=partner.name.replace(/  +/g, ' ').split(' ');
        if(partner_name.length > 1){
            partner.name=partner_name[0];
            partner.lastName='';
            if(partner_name.length>1)
            for(var i=1;i<partner_name.length;i++)
                {
                    partner.lastName=partner.lastName+" "+partner_name[i];
                }
        }
        this.display_client_details('edit',partner);
    },

    });

    //To change product limit in pos session
    posDbCustom = posDb.include({
        init: function () {
            this.limit = 250;
            this._super();
        },
        
        _product_search_string: function(product){
        var str = product.display_name;
        if (product.barcode) {
            str += '|' + product.barcode;
        }
        if (product.default_code) {
            str += '|' + product.default_code;
        }
//         if (product.description) {
//             str += '|' + product.description;
//         }
//         if (product.description_sale) {
//             str += '|' + product.description_sale;
//         }
        str  = product.id + ':' + str.replace(/:/g,'') + '\n';
        return str;
    },
        
        search_product_in_category: function(category_id, query){
        try {
            query = query.replace(/[\[\]\(\)\+\*\?\.\-\!\&\^\$\|\~\_\{\}\:\,\\\/]/g,'.');
            query = query.replace(/ /g,'.+');
            var re = RegExp("([0-9]+):.*?"+query,"gi");
            var temporaryArray=[];
        }catch(e){
            return [];
        }
        var results = [];
        for(var i = 0; i < this.limit; i++){
            var r = re.exec(this.category_search_string[category_id]);
            if(r){
                temporaryArray.push(r);
               
            }else{
                break;
            }
        }
        //Temporary array to sort
        temporaryArray.sort(function(a,b) {
        return a[0].toLowerCase().indexOf(query) - b[0].toLowerCase().indexOf(query);
        })
            
        for(var i=0;i<temporaryArray.length;i++)
        {
            var id = Number(temporaryArray[i][1]);
            results.push(this.get_product_by_id(id));     
        }
            
        return results;
    },

    });
    
});