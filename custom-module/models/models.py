# -*- coding: utf-8 -*-


from odoo import models, fields, api
# class custom-module(models.Model):
#     _name = 'custom-module.custom-module'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

class PosCustomConfig(models.Model):
    _inherit = 'pos.config'
    # Methods to open the POS
    @api.multi
    def open_ui(self):
        self.ensure_one()
        # check all constraints, raises if any is not met
        self._validate_fields(self._fields)
        return {
            'type': 'ir.actions.act_url',
            'url':   '/pos/web/?iotbox=1',
            'target': 'self',
        }

class productCustom(models.Model):
    _inherit = 'product.product'
    
    #product_company = fields.Many2one('res.company', 'Company', related='product_tmpl_id.company_id', store=True)

    #_sql_constraints = [ ('barcode_uniq', 'unique(product_company, barcode)', ("Barcode should be unique by company!")), ]
    
    @api.model
    def _auto_init(self):
     res = super(productCustom, self)._auto_init()
     self._sql_constraints = [('barcode_uniq', 'unique(company_id, barcode)', ("Barcode should be unique by company!"))]
     return res