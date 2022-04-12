import string
from odoo import api,fields,models,_


class SaleOrder(models.Model):
    _inherit = "sale.order"

    # Fields declarations
    zero_stock_approval = fields.Boolean(string="Approval")

