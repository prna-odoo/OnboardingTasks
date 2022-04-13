from odoo import api,models


class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.model
    def create(self, vals):
        print("\n valsssssssssss====", vals)
        if vals.get('name'):
            if vals['customer_rank']:
                if vals['customer_rank'] > 0:
                    print("\n ifffffffffffff", vals['ref'])
                    vals['ref'] = self.env['ir.sequence'].next_by_code('customer.sequence') or '/'
            elif vals['supplier_rank']:
                if vals['supplier_rank'] > 0:
                    vals['ref'] = self.env['ir.sequence'].next_by_code('supplier.sequence') or '/'
                    print("\n ifffffffffffff afterrrrrrrrrr", vals['ref'])
        return super().create(vals)

