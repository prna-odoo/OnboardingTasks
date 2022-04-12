from odoo import fields,models

class ResPartner(models.Model):
    _inherit = "res.partner"

    #Field declaration
    inventory_line_ids = fields.One2many("inventory.line","partner_id")


