# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    mg_arrives = fields.Char('mg_arrives')
    mg_asin = fields.Char('mg_asin')
    mg_assembly_required = fields.Char('mg_assembly_required')
    mg_bed_size = fields.Char('mg_bed_size')
    mg_bed_type = fields.Char('mg_bed_type')
    mg_boxspring = fields.Char('mg_bom')
    mg_bom = fields.Char('mg_boxspring')
    mg_canonical_cross_domain = fields.Char('mg_canonical_cross_domain')
    mg_canonical_url = fields.Char('mg_canonical_url')
    mg_carton_height = fields.Char('mg_carton_height')
    mg_carton_length = fields.Char('mg_carton_length')
    mg_carton_width = fields.Char('mg_carton_width')
    mg_child_category = fields.Char('mg_child_category')
    mg_collections = fields.Char('mg_collections')
    mg_color = fields.Char('mg_color')
    mg_color_base = fields.Char('mg_color_base')
    mg_comfort_level = fields.Char('mg_comfort_level')
    mg_cost = fields.Char('mg_cost')
    mg_country_of_manufacture = fields.Char('mg_country_of_manufacture')
    mg_cube = fields.Char('mg_cube')
    mg_depth = fields.Char('mg_depth')
    mg_description = fields.Char('mg_description')
    mg_feature_eight = fields.Char('mg_feature_eight')
    mg_feature_eleven = fields.Char('mg_feature_eleven')
    mg_feature_fifteen = fields.Char('mg_feature_fifteen')
    mg_feature_five = fields.Char('mg_feature_five')
    mg_feature_four = fields.Char('mg_feature_four')
    mg_feature_fourteen = fields.Char('mg_feature_fourteen')
    mg_feature_nine = fields.Char('mg_feature_nine')
    mg_feature_one = fields.Char('mg_feature_one')
    mg_feature_seven = fields.Char('mg_feature_seven')
    mg_feature_six = fields.Char('mg_feature_six')
    mg_feature_ten = fields.Char('mg_feature_ten')
    mg_feature_thirteen = fields.Char('mg_feature_thirteen')
    mg_feature_three = fields.Char('mg_feature_three')
    mg_feature_twelve = fields.Char('mg_feature_twelve')
    mg_feature_two = fields.Char('mg_feature_two')
    mg_free_shipping_discount = fields.Char('mg_free_shipping_discount')
    mg_height = fields.Char('mg_height')
    mg_includes = fields.Char('mg_includes')
    mg_include_skus = fields.Char('mg_include_skus')
    mg_is_bundle = fields.Char('mg_is_bundle')
    mg_length = fields.Char('mg_length')
    mg_length_one = fields.Char('mg_length_one')
    mg_lowest_price = fields.Char('mg_lowest_price')
    mg_manufacturer = fields.Char('mg_manufacturer')
    mg_manufacturer_product_code = fields.Char('mg_manufacturer_product_code')
    mg_material = fields.Char('mg_material')
    mg_mattress_size = fields.Char('mg_mattress_size')
    mg_mattress_type = fields.Char('mg_mattress_type')
    mg_motion_type = fields.Char('mg_motion_type')
    mg_msrp = fields.Char('mg_msrp')
    mg_multiple_options = fields.Char('mg_multiple_options')
    mg_on_sale = fields.Char('mg_on_sale')
    mg_parent_category = fields.Char('mg_parent_category')
    mg_part_number = fields.Char('mg_part_number')
    mg_price = fields.Char('mg_price')
    mg_productvideo = fields.Char('mg_productvideo')
    mg_product_id = fields.Char('mg_product_id')
    mg_product_type = fields.Char('mg_product_type')
    mg_profit_margin_dollar = fields.Char('mg_profit_margin_dollar')
    mg_profit_margin_percentage = fields.Char('mg_profit_margin_percentage')
    mg_seat_depth = fields.Char('mg_seat_depth')
    mg_seat_height = fields.Char('mg_seat_height')
    mg_shipping_information = fields.Char('mg_shipping_information')
    mg_sofa_fabrics = fields.Char('mg_sofa_fabrics')
    mg_sofa_type = fields.Char('mg_sofa_type')
    mg_starting_at = fields.Char('mg_starting_at')
    mg_styles = fields.Char('mg_styles')
    mg_table_base_type = fields.Char('mg_table_base_type')
    mg_table_height = fields.Char('mg_table_height')
    mg_table_top_materials = fields.Char('mg_table_top_materials')
    mg_table_top_shapes = fields.Char('mg_table_top_shapes')
    mg_upc = fields.Char('mg_upc')
    mg_url_key = fields.Char('mg_url_key')
    mg_url_path = fields.Char('mg_url_path')
    mg_vendor_description = fields.Char('mg_vendor_description')
    mg_volume_weight = fields.Char('mg_volume_weight')
    mg_warranty = fields.Char('mg_warranty')
    mg_weight = fields.Char('mg_weight')
    mg_width = fields.Char('mg_width')

    @api.multi
    @api.constrains('mg_bom','mg_carton_height','mg_carton_width','mg_carton_length','mg_weight','mg_cube','mg_url_path')
    def magento_map_update(self):
        for record in self:
            vals = {
                'bom_parser':record.mg_bom,
                'carton_height':float(record.mg_carton_height) or False,
                'carton_width':float(record.mg_carton_width) or False,
                'length':float(record.mg_carton_length) or False,
                'weight':float(record.mg_weight) or False,
                'volume':float(record.mg_cube) or False,
                'manu_url': ("http://www.localfurnitureoutlet.com/" + record.mg_url_path),
            }
            record.write(vals)
