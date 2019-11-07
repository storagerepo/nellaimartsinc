odoo.define('pos_custom_model', function (require) {

var module = require('point_of_sale.models');
var PosBaseWidget = require('point_of_sale.BaseWidget');
var models = module.PosModel.prototype.models;
for(var i=0; i<models.length; i++){
    var model=models[i];
    if(model.model === 'res.company'){
         model.fields.push('street');
         model.fields.push('city');
         model.fields.push('state_id');
         model.fields.push('country_id');
    } 
}
 //To remove $ in subtotal   
    PosBaseWidgetCustom = PosBaseWidget.include({
    format_currency_custom: function(amount,precision){

        amount = this.format_currency(amount,precision);
        amount=amount.replace(' ','');
        console.log(amount);
        return amount;
    }
})
});

odoo.define('pos_keyboard_shortcut',function(require){
    "user strict"
    $(document).addEventListener('keydown', function(event) {
    if(event.keyCode == 8) {
        self.gui.back();
    }
    else if(event.keyCode == 80) {
     $(".pay").click();
    }
    })   
})

