var module = require('point_of_sale.models');
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