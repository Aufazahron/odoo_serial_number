
from odoo import api, fields, models

class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    custom_serial_number = fields.Char(string="Custom Serial Number", readonly=True)

    @api.model
    def create(self, vals):
        # Retrieve product_id from Manufacturing Order
        product_id = vals.get('product_id')
        if product_id:
            product = self.env['product.product'].browse(product_id)
            
            # Define prefix based on product name
            if product.name == 'PC Full Set':
                prefix = 'CA'
            elif product.name == 'PC Tanpa Monitor':
                prefix = 'CB'
            else:
                prefix = 'XX'  # Default prefix for other products

            # Get the next sequence number using the sequence code
            sequence_code = f'serial.number.{prefix.lower()}'
            serial_number = self.env['ir.sequence'].next_by_code(sequence_code)

            # Combine prefix and sequence number for the final serial number
            vals['custom_serial_number'] = f"{prefix}{serial_number}"

        return super(MrpProduction, self).create(vals)
