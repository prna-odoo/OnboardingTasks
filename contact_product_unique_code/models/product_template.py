from odoo import api,models

class ProductTemplate(models.Model):
    _inherit = "product.template"

    def get_parent_id(self , categ_id):
            if categ_id and categ_id.sequence_new.id:
                return categ_id.sequence_new
            elif categ_id.parent_id :
                return self.get_parent_id(categ_id.parent_id)
            else:
                return False

    @api.model
    def create(self, vals):
        vals=super().create(vals)
        print("#############33",vals)
        if vals.categ_id and vals.categ_id.sequence_new:
            vals.default_code = vals.categ_id.sequence_new.next_by_id()
        else:
            seq = vals.get_parent_id(vals.categ_id.parent_id)
            vals.default_code = seq.next_by_id()
        return vals