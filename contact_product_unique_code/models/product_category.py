from odoo import fields,models

class ProductCategory(models.Model):
    _inherit = "product.category"

    #Field declaration 
    assign_sequence = fields.Boolean(string="Assign squence")
    sequence_new = fields.Many2one("ir.sequence",string="Sequence") 

