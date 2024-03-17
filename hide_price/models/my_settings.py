# from odoo import fields, models, api

# class UserExtension(models.Model):
#     _inherit = "res.users"

#     cost_price = fields.Boolean(string="Show Cost Price")
#     sale_price = fields.Boolean(string="Show Sale Price")


    # @api.onchange('sale_price')
    # def _onchange_sale_price(self):

    #     if self.sale_price:

    #         self.env['ir.ui.view'].search([('name', '=', 'kanban_sale_price')]).write({'arch': '<xpath expr="//div[@name=\'product_lst_price\']" position="attributes"><attribute name="invisible">0</attribute></xpath>'})
    #         self.env['ir.ui.view'].search([('name', '=', 'product.tree.sale.inherited')]).write({'arch':'<xpath expr="//field[@name=\'list_price\']" position="attributes"><attribute name="invisible">0</attribute></xpath>'})
    #         # Sale price form view
    #         self.env['ir.ui.view'].search([('name', '=', 'product.form.sale.price.inherited')]).write({'arch': '<xpath expr="//group[@name=\'group_standard_price\']/label[@for=\'list_price\']" position="attributes"><attribute name="invisible">0</attribute></xpath>'})
    #         self.env['ir.ui.view'].search([('name', '=', 'product.form.sale.price.inherited')]).write({'arch': '
    #         # sale price product variant tree<xpath expr="//group[@name=\'group_standard_price\']/div[@name=\'pricing\']" position="attributes"><attribute name="invisible">0</attribute></xpath>'})
    #         # self.env['ir.ui.view'].search([('name', '=', 'product_variant_sale_tree')]).write({'arch':'<xpath expr="//field[@name=\'lst_price\']" position="attributes"><attribute name="invisible">0</attribute></xpath> '})
    #         # sale price product variant kanban
    #         # self.env['ir.ui.view'].search([('name', '=', 'product.variant.kanban.inherited')]).write({'arch':'<xpath expr="//ul/li/strong[field/@name=\'lst_price\']" position="attributes"><attribute name="invisible">0</attribute></xpath>'})
    #         # sale price purchase form 
    #         self.env['ir.ui.view'].search([('name', '=', 'product.purchase.template.form')]).write({'arch': '''<xpath expr="//page[@name=\'purchase\']" position="inside">
    #         <field name="seller_ids" invisible="1"/>
               
    #         <group name="bill" invisible="1">
    #     <field name="seller_ids" invisible="0">
    #       <tree>
    #                 <field name="name" invisible="0"/>
    #                 <field name="price" invisible="0"/>
    #                 <field name="currency_id" invisible="0"/>
    #                 <field name="delay" invisible="0"/>
    #             </tree>
    #             </field>
    # </group>
    #         </xpath>'''})


                 
    #     else:

    #         self.env['ir.ui.view'].search([('name', '=', 'kanban_sale_price')]).write({'arch': '<xpath expr="//div[@name=\'product_lst_price\']" position="attributes"><attribute name="invisible">1</attribute></xpath>'})
    #         self.env['ir.ui.view'].search([('name', '=', 'product.tree.sale.inherited')]).write({'arch':'<xpath expr="//field[@name=\'list_price\']" position="attributes"><attribute name="invisible">1</attribute></xpath>'})
    #     #   sale price form view 
    #         self.env['ir.ui.view'].search([('name', '=', 'product.form.sale.price.inherited')]).write({'arch': '<xpath expr="//group[@name=\'group_standard_price\']/label[@for=\'list_price\']" position="attributes"><attribute name="invisible">1</attribute></xpath>'})
    #         self.env['ir.ui.view'].search([('name', '=', 'product.form.sale.price.inherited')]).write({'arch': '<xpath expr="//group[@name=\'group_standard_price\']/div[@name=\'pricing\']" position="attributes"><attribute name="invisible">1</attribute></xpath>'})
    #         # sale price product variant tree
    #         # self.env['ir.ui.view'].search([('name', '=', 'product_variant_sale_tree')]).write({'arch':'<xpath expr="//field[@name=\'lst_price\']" position="attributes"><attribute name="invisible">1</attribute></xpath> '})
    #         # sale price product variant kanban
    #         # self.env['ir.ui.view'].search([('name', '=', 'product.variant.kanban.inherited')]).write({'arch':'<xpath expr="//ul/li/strong[field/@name=\'lst_price\']" position="attributes"><attribute name="invisible">1</attribute></xpath>'})
    #         # sale price purchase view
    #         self.env['ir.ui.view'].search([('name', '=', 'product.purchase.template.form')]).write({'arch': '''<xpath expr="//page[@name=\'purchase\']" position="inside">
    #         <field name="seller_ids" invisible="1"/>
               
    #         <group name="bill" invisible="1">
    #     <field name="seller_ids" invisible="0">
    #       <tree>
    #                 <field name="name" invisible="0"/>
    #                 <field name="price" invisible="1"/>
    #                 <field name="currency_id" invisible="1"/>
    #                 <field name="delay" invisible="0"/>
    #             </tree>
    #             </field>
    # </group>
    #         </xpath>'''})


            


    # @api.onchange('cost_price')
    # def _onchange_cost_price(self):
    #     if self.cost_price:

    #         # tree product price
    #         self.env['ir.ui.view'].search([('name', '=', 'product.tree.cost.inherited')]).write({'arch':'<xpath expr="//field[@name=\'standard_price\']" position="attributes"><attribute name="invisible">0</attribute></xpath>'})
    #         # form product price
    #         self.env['ir.ui.view'].search([('name', '=', 'product.form.cost.price.inherited')]).write({'arch': '<xpath expr="//group[@name=\'group_standard_price\']/label[@for=\'standard_price\']" position="attributes"><attribute name="invisible">0</attribute></xpath>'})
    #         self.env['ir.ui.view'].search([('name', '=', 'product.form.cost.price.inherited')]).write({'arch': '<xpath expr="//group[@name=\'group_standard_price\']/div[@name=\'standard_price_uom\']" position="attributes"><attribute name="invisible">0</attribute></xpath>'})
    #         # cost price product variant tree
    #         # self.env['ir.ui.view'].search([('name', '=', 'product_variant_cost_tree')]).write({'arch':'<xpath expr="//field[@name=\'standard_price\']" position="attributes"><attribute name="invisible">0</attribute></xpath> '})


    #     else:

    #         # tree product price
    #         self.env['ir.ui.view'].search([('name', '=', 'product.tree.cost.inherited')]).write({'arch':'<xpath expr="//field[@name=\'standard_price\']" position="attributes"><attribute name="invisible">1</attribute></xpath>'})
    #         # form product price
    #         self.env['ir.ui.view'].search([('name', '=', 'product.form.cost.price.inherited')]).write({'arch': '<xpath expr="//group[@name=\'group_standard_price\']/label[@for=\'standard_price\']" position="attributes"><attribute name="invisible">1</attribute></xpath>'})
    #         self.env['ir.ui.view'].search([('name', '=', 'product.form.cost.price.inherited')]).write({'arch': '<xpath expr="//group[@name=\'group_standard_price\']/div[@name=\'standard_price_uom\']" position="attributes"><attribute name="invisible">1</attribute></xpath>'})
    #         # cost price product variant tree
    #         # self.env['ir.ui.view'].search([('name', '=', 'product_variant_cost_tree')]).write({'arch':'<xpath expr="//field[@name=\'standard_price\']" position="attributes"><attribute name="invisible">1</attribute></xpath> '})





    # @api.onchange('sale_price', 'cost_price')
    # def _onchange_sale_cost_price(self):

    #     if self.sale_price and self.cost_price:

    #         self.env['ir.ui.view'].search([('name', '=', 'kanban_sale_price')]).write({'arch': '<xpath expr="//div[@name=\'product_lst_price\']" position="attributes"><attribute name="invisible">0</attribute></xpath>'})
    #         self.env['ir.ui.view'].search([('name', '=', 'product.tree.sale.inherited')]).write({'arch':'<xpath expr="//field[@name=\'list_price\']" position="attributes"><attribute name="invisible">0</attribute></xpath>'})
    #         # Sale price form view
    #         self.env['ir.ui.view'].search([('name', '=', 'product.form.sale.price.inherited')]).write({'arch': '<xpath expr="//group[@name=\'group_standard_price\']/label[@for=\'list_price\']" position="attributes"><attribute name="invisible">0</attribute></xpath>'})
    #         self.env['ir.ui.view'].search([('name', '=', 'product.form.sale.price.inherited')]).write({'arch': '<xpath expr="//group[@name=\'group_standard_price\']/div[@name=\'pricing\']" position="attributes"><attribute name="invisible">0</attribute></xpath>'})
    #         # sale price product variant tree
    #         # self.env['ir.ui.view'].search([('name', '=', 'product_variant_sale_tree')]).write({'arch':'<xpath expr="//field[@name=\'lst_price\']" position="attributes"><attribute name="invisible">0</attribute></xpath> '})
    #         # sale price product variant kanban
    #         # self.env['ir.ui.view'].search([('name', '=', 'product.variant.kanban.inherited')]).write({'arch':'<xpath expr="//ul/li/strong[field/@name=\'lst_price\']" position="attributes"><attribute name="invisible">0</attribute></xpath>'})
    #         # sale price purchase form 
    #         self.env['ir.ui.view'].search([('name', '=', 'product.purchase.template.form')]).write({'arch': '''<xpath expr="//page[@name=\'purchase\']" position="inside">
    #         <field name="seller_ids" invisible="1"/>
               
    #         <group name="bill" invisible="1">
    #     <field name="seller_ids" invisible="0">
    #       <tree>
    #                 <field name="name" invisible="0"/>
    #                 <field name="price" invisible="0"/>
    #                 <field name="currency_id" invisible="0"/>
    #                 <field name="delay" invisible="0"/>
    #             </tree>
    #             </field>
    # </group>
    #         </xpath>'''})

    #          # tree product price
    #         self.env['ir.ui.view'].search([('name', '=', 'product.tree.cost.inherited')]).write({'arch':'<xpath expr="//field[@name=\'standard_price\']" position="attributes"><attribute name="invisible">0</attribute></xpath>'})
    #         # form product price
    #         self.env['ir.ui.view'].search([('name', '=', 'product.form.cost.price.inherited')]).write({'arch': '<xpath expr="//group[@name=\'group_standard_price\']/label[@for=\'standard_price\']" position="attributes"><attribute name="invisible">0</attribute></xpath>'})
    #         self.env['ir.ui.view'].search([('name', '=', 'product.form.cost.price.inherited')]).write({'arch': '<xpath expr="//group[@name=\'group_standard_price\']/div[@name=\'standard_price_uom\']" position="attributes"><attribute name="invisible">0</attribute></xpath>'})
    #         # cost price product variant tree
    #         # self.env['ir.ui.view'].search([('name', '=', 'product_variant_cost_tree')]).write({'arch':'<xpath expr="//field[@name=\'standard_price\']" position="attributes"><attribute name="invisible">0</attribute></xpath> '})
    #     else:
    #         self.env['ir.ui.view'].search([('name', '=', 'kanban_sale_price')]).write({'arch': '<xpath expr="//div[@name=\'product_lst_price\']" position="attributes"><attribute name="invisible">1</attribute></xpath>'})
    #         self.env['ir.ui.view'].search([('name', '=', 'product.tree.sale.inherited')]).write({'arch':'<xpath expr="//field[@name=\'list_price\']" position="attributes"><attribute name="invisible">1</attribute></xpath>'})
    #         #sale price form view 
    #         self.env['ir.ui.view'].search([('name', '=', 'product.form.sale.price.inherited')]).write({'arch': '<xpath expr="//group[@name=\'group_standard_price\']/label[@for=\'list_price\']" position="attributes"><attribute name="invisible">1</attribute></xpath>'})
    #         self.env['ir.ui.view'].search([('name', '=', 'product.form.sale.price.inherited')]).write({'arch': '<xpath expr="//group[@name=\'group_standard_price\']/div[@name=\'pricing\']" position="attributes"><attribute name="invisible">1</attribute></xpath>'})
    #         # sale price product variant tree
    #         # self.env['ir.ui.view'].search([('name', '=', 'product_variant_sale_tree')]).write({'arch':'<xpath expr="//field[@name=\'lst_price\']" position="attributes"><attribute name="invisible">1</attribute></xpath> '})
    #         # sale price product variant kanban
    #         # self.env['ir.ui.view'].search([('name', '=', 'product.variant.kanban.inherited')]).write({'arch':'<xpath expr="//ul/li/strong[field/@name=\'lst_price\']" position="attributes"><attribute name="invisible">1</attribute></xpath>'})
    #         # sale price purchase view
    #         self.env['ir.ui.view'].search([('name', '=', 'product.purchase.template.form')]).write({'arch': '''<xpath expr="//page[@name=\'purchase\']" position="inside">
    #         <field name="seller_ids" invisible="1"/>
               
    #         <group name="bill" invisible="1">
    #     <field name="seller_ids" invisible="0">
    #       <tree>
    #                 <field name="name" invisible="0"/>
    #                 <field name="price" invisible="1"/>
    #                 <field name="currency_id" invisible="1"/>
    #                 <field name="delay" invisible="0"/>
    #             </tree>
    #             </field>
    # </group>
    #         </xpath>'''})



    #         # tree product price
    #         self.env['ir.ui.view'].search([('name', '=', 'product.tree.cost.inherited')]).write({'arch':'<xpath expr="//field[@name=\'standard_price\']" position="attributes"><attribute name="invisible">1</attribute></xpath>'})
    #         # form product price
    #         self.env['ir.ui.view'].search([('name', '=', 'product.form.cost.price.inherited')]).write({'arch': '<xpath expr="//group[@name=\'group_standard_price\']/label[@for=\'standard_price\']" position="attributes"><attribute name="invisible">1</attribute></xpath>'})
    #         self.env['ir.ui.view'].search([('name', '=', 'product.form.cost.price.inherited')]).write({'arch': '<xpath expr="//group[@name=\'group_standard_price\']/div[@name=\'standard_price_uom\']" position="attributes"><attribute name="invisible">1</attribute></xpath>'})
    #         # cost price product variant tree
    #         # self.env['ir.ui.view'].search([('name', '=', 'product_variant_cost_tree')]).write({'arch':'<xpath expr="//field[@name=\'standard_price\']" position="attributes"><attribute name="invisible">1</attribute></xpath> '})






from odoo import fields, models, api

class UserExtension(models.Model):
    _inherit = "res.users"

    cost_price = fields.Boolean(string="Show Cost Price")
    sale_price = fields.Boolean(string="Show Sale Price")

    @api.onchange('sale_price')
    def onchange_sale_price(self):
        if self.sale_price:
            self.env['ir.ui.view'].search([('name', '=', 'kanban_sale_price')]).write({'arch': '<xpath expr="//div[@name=\'product_lst_price\']" position="attributes"><attribute name="invisible">0</attribute></xpath>'})
            self.env['ir.ui.view'].search([('name', '=', 'product.tree.sale.inherited')]).write({'arch': '<xpath expr="//field[@name=\'list_price\']" position="attributes"><attribute name="invisible">0</attribute></xpath>'})
            self.env['ir.ui.view'].search([('name', '=', 'product.form.sale.price.inherited')]).write({'arch': '<xpath expr="//group[@name=\'group_standard_price\']/label[@for=\'list_price\']" position="attributes"><attribute name="invisible">0</attribute></xpath>'})
            self.env['ir.ui.view'].search([('name', '=', 'product.form.sale.price.inherited')]).write({'arch': '<xpath expr="//group[@name=\'group_standard_price\']/div[@name=\'pricing\']" position="attributes"><attribute name="invisible">0</attribute></xpath>'})
            self.env['ir.ui.view'].search([('name', '=', 'product.purchase.template.form')]).write({'arch':  '''<xpath expr="//page[@name=\'purchase\']" position="inside">
                <field name="seller_ids" invisible="1"/>
                
                <group name="bill" invisible="1">
            <field name="seller_ids" invisible="0">
            <tree>
                        <field name="name" invisible="0"/>
                        <field name="price" invisible="0"/>
                        <field name="currency_id" invisible="0"/>
                        <field name="delay" invisible="0"/>
                    </tree>
                    </field>
        </group>
                </xpath>'''})

        else:
            self.env['ir.ui.view'].search([('name', '=', 'kanban_sale_price')]).write({'arch': '<xpath expr="//div[@name=\'product_lst_price\']" position="attributes"><attribute name="invisible">1</attribute></xpath>'})
            self.env['ir.ui.view'].search([('name', '=', 'product.tree.sale.inherited')]).write({'arch': '<xpath expr="//field[@name=\'list_price\']" position="attributes"><attribute name="invisible">1</attribute></xpath>'})
            self.env['ir.ui.view'].search([('name', '=', 'product.form.sale.price.inherited')]).write({'arch': '<xpath expr="//group[@name=\'group_standard_price\']/label[@for=\'list_price\']" position="attributes"><attribute name="invisible">1</attribute></xpath>'})
            self.env['ir.ui.view'].search([('name', '=', 'product.form.sale.price.inherited')]).write({'arch': '<xpath expr="//group[@name=\'group_standard_price\']/div[@name=\'pricing\']" position="attributes"><attribute name="invisible">1</attribute></xpath>'})
            self.env['ir.ui.view'].search([('name', '=', 'product.purchase.template.form')]).write({'arch':  '''<xpath expr="//page[@name=\'purchase\']" position="inside">
                <field name="seller_ids" invisible="1"/>
                
                <group name="bill" invisible="1">
            <field name="seller_ids" invisible="0">
            <tree>
                        <field name="name" invisible="0"/>
                        <field name="price" invisible="1"/>
                        <field name="currency_id" invisible="1"/>
                        <field name="delay" invisible="0"/>
                    </tree>
                    </field>
        </group>
                </xpath>'''})


    @api.onchange('cost_price')
    def onchange_cost_price(self):
        if self.cost_price:
            self.env['ir.ui.view'].search([('name', '=', 'product.tree.cost.inherited')]).write({'arch': '<xpath expr="//field[@name=\'standard_price\']" position="attributes"><attribute name="invisible">0</attribute></xpath>'})
            self.env['ir.ui.view'].search([('name', '=', 'product.form.cost.price.inherited')]).write({'arch': '<xpath expr="//group[@name=\'group_standard_price\']/label[@for=\'standard_price\']" position="attributes"><attribute name="invisible">0</attribute></xpath>'})
            self.env['ir.ui.view'].search([('name', '=', 'product.form.cost.price.inherited')]).write({'arch': '<xpath expr="//group[@name=\'group_standard_price\']/div[@name=\'standard_price_uom\']" position="attributes"><attribute name="invisible">0</attribute></xpath>'})
        else:
            self.env['ir.ui.view'].search([('name', '=', 'product.tree.cost.inherited')]).write({'arch': '<xpath expr="//field[@name=\'standard_price\']" position="attributes"><attribute name="invisible">1</attribute></xpath>'})
            self.env['ir.ui.view'].search([('name', '=', 'product.form.cost.price.inherited')]).write({'arch': '<xpath expr="//group[@name=\'group_standard_price\']/label[@for=\'standard_price\']" position="attributes"><attribute name="invisible">1</attribute></xpath>'})
            self.env['ir.ui.view'].search([('name', '=', 'product.form.cost.price.inherited')]).write({'arch': '<xpath expr="//group[@name=\'group_standard_price\']/div[@name=\'standard_price_uom\']" position="attributes"><attribute name="invisible">1</attribute></xpath> '})


    @api.onchange('cost_price', 'sale_price')
    def onchange_both_prices(self):
        if self.cost_price and self.sale_price:
            # Make both cost price and sale price views visible
            self.env['ir.ui.view'].search([('name', '=', 'kanban_sale_price')]).write({'arch': '<xpath expr="//div[@name=\'product_lst_price\']" position="attributes"><attribute name="invisible">0</attribute></xpath> '})
            self.env['ir.ui.view'].search([('name', '=', 'product.tree.sale.inherited')]).write({'arch': '<xpath expr="//field[@name=\'list_price\']" position="attributes"><attribute name="invisible">0</attribute></xpath>'})
            self.env['ir.ui.view'].search([('name', '=', 'product.form.sale.price.inherited')]).write({'arch': '<xpath expr="//group[@name=\'group_standard_price\']/label[@for=\'list_price\']" position="attributes"><attribute name="invisible">0</attribute></xpath>'})
            self.env['ir.ui.view'].search([('name', '=', 'product.form.sale.price.inherited')]).write({'arch': '<xpath expr="//group[@name=\'group_standard_price\']/div[@name=\'pricing\']" position="attributes"><attribute name="invisible">0</attribute></xpath> '})
            self.env['ir.ui.view'].search([('name', '=', 'product.purchase.template.form')]).write({'arch':  '''<xpath expr="//page[@name=\'purchase\']" position="inside">
                <field name="seller_ids" invisible="1"/>
                
                <group name="bill" invisible="1">
            <field name="seller_ids" invisible="0">
            <tree>
                        <field name="name" invisible="0"/>
                        <field name="price" invisible="0"/>
                        <field name="currency_id" invisible="0"/>
                        <field name="delay" invisible="0"/>
                    </tree>
                    </field>
        </group>
                </xpath>'''})
            
            self.env['ir.ui.view'].search([('name', '=', 'product.tree.cost.inherited')]).write({'arch': '<xpath expr="//field[@name=\'standard_price\']" position="attributes"><attribute name="invisible">0</attribute></xpath>'})
            self.env['ir.ui.view'].search([('name', '=', 'product.form.cost.price.inherited')]).write({'arch': '<xpath expr="//group[@name=\'group_standard_price\']/label[@for=\'standard_price\']" position="attributes"><attribute name="invisible">0</attribute></xpath>'})
            self.env['ir.ui.view'].search([('name', '=', 'product.form.cost.price.inherited')]).write({'arch': '<xpath expr="//group[@name=\'group_standard_price\']/div[@name=\'standard_price_uom\']" position="attributes"><attribute name="invisible">0</attribute></xpath>'})
            # Make both cost price and sale price views invisible


        elif not self.cost_price and self.sale_price:
            self.env['ir.ui.view'].search([('name', '=', 'kanban_sale_price')]).write({'arch': '<xpath expr="//div[@name=\'product_lst_price\']" position="attributes"><attribute name="invisible">0</attribute></xpath>'})
            self.env['ir.ui.view'].search([('name', '=', 'product.tree.sale.inherited')]).write({'arch': '<xpath expr="//field[@name=\'list_price\']" position="attributes"><attribute name="invisible">0</attribute></xpath>'})
            self.env['ir.ui.view'].search([('name', '=', 'product.form.sale.price.inherited')]).write({'arch': '<xpath expr="//group[@name=\'group_standard_price\']/label[@for=\'list_price\']" position="attributes"><attribute name="invisible">0</attribute></xpath>'})
            self.env['ir.ui.view'].search([('name', '=', 'product.form.sale.price.inherited')]).write({'arch': '<xpath expr="//group[@name=\'group_standard_price\']/div[@name=\'pricing\']" position="attributes"><attribute name="invisible">0</attribute></xpath>'})
            self.env['ir.ui.view'].search([('name', '=', 'product.purchase.template.form')]).write({'arch':  '''<xpath expr="//page[@name=\'purchase\']" position="inside">
                <field name="seller_ids" invisible="1"/>
                
                <group name="bill" invisible="1">
            <field name="seller_ids" invisible="0">
            <tree>
                        <field name="name" invisible="0"/>
                        <field name="price" invisible="0"/>
                        <field name="currency_id" invisible="0"/>
                        <field name="delay" invisible="0"/>
                    </tree>
                    </field>
        </group>
                </xpath>'''})
            
            self.env['ir.ui.view'].search([('name', '=', 'product.tree.cost.inherited')]).write({'arch': '<xpath expr="//field[@name=\'standard_price\']" position="attributes"><attribute name="invisible">1</attribute></xpath>'})
            self.env['ir.ui.view'].search([('name', '=', 'product.form.cost.price.inherited')]).write({'arch': '<xpath expr="//group[@name=\'group_standard_price\']/label[@for=\'standard_price\']" position="attributes"><attribute name="invisible">1</attribute></xpath>'})
            self.env['ir.ui.view'].search([('name', '=', 'product.form.cost.price.inherited')]).write({'arch': '<xpath expr="//group[@name=\'group_standard_price\']/div[@name=\'standard_price_uom\']" position="attributes"><attribute name="invisible">1</attribute></xpath> '})

        elif  self.cost_price and not self.sale_price:
            self.env['ir.ui.view'].search([('name', '=', 'kanban_sale_price')]).write({'arch': '<xpath expr="//div[@name=\'product_lst_price\']" position="attributes"><attribute name="invisible">1</attribute></xpath>'})
            self.env['ir.ui.view'].search([('name', '=', 'product.tree.sale.inherited')]).write({'arch': '<xpath expr="//field[@name=\'list_price\']" position="attributes"><attribute name="invisible">1</attribute></xpath>'})
            self.env['ir.ui.view'].search([('name', '=', 'product.form.sale.price.inherited')]).write({'arch': '<xpath expr="//group[@name=\'group_standard_price\']/label[@for=\'list_price\']" position="attributes"><attribute name="invisible">1</attribute></xpath>'})
            self.env['ir.ui.view'].search([('name', '=', 'product.form.sale.price.inherited')]).write({'arch': '<xpath expr="//group[@name=\'group_standard_price\']/div[@name=\'pricing\']" position="attributes"><attribute name="invisible">1</attribute></xpath>'})
            self.env['ir.ui.view'].search([('name', '=', 'product.purchase.template.form')]).write({'arch':  '''<xpath expr="//page[@name=\'purchase\']" position="inside">
                <field name="seller_ids" invisible="1"/>
                
                <group name="bill" invisible="1">
            <field name="seller_ids" invisible="0">
            <tree>
                        <field name="name" invisible="0"/>
                        <field name="price" invisible="1"/>
                        <field name="currency_id" invisible="1"/>
                        <field name="delay" invisible="0"/>
                    </tree>
                    </field>
        </group>
                </xpath>'''})
            
            self.env['ir.ui.view'].search([('name', '=', 'product.tree.cost.inherited')]).write({'arch': '<xpath expr="//field[@name=\'standard_price\']" position="attributes"><attribute name="invisible">0</attribute></xpath>'})
            self.env['ir.ui.view'].search([('name', '=', 'product.form.cost.price.inherited')]).write({'arch': '<xpath expr="//group[@name=\'group_standard_price\']/label[@for=\'standard_price\']" position="attributes"><attribute name="invisible">0</attribute></xpath>'})
            self.env['ir.ui.view'].search([('name', '=', 'product.form.cost.price.inherited')]).write({'arch': '<xpath expr="//group[@name=\'group_standard_price\']/div[@name=\'standard_price_uom\']" position="attributes"><attribute name="invisible">0</attribute></xpath>'})

        else:    
            self.env['ir.ui.view'].search([('name', '=', 'kanban_sale_price')]).write({'arch': '<xpath expr="//div[@name=\'product_lst_price\']" position="attributes"><attribute name="invisible">1</attribute></xpath> '})
            self.env['ir.ui.view'].search([('name', '=', 'product.tree.sale.inherited')]).write({'arch': '<xpath expr="//field[@name=\'list_price\']" position="attributes"><attribute name="invisible">1</attribute></xpath>'})
            self.env['ir.ui.view'].search([('name', '=', 'product.form.sale.price.inherited')]).write({'arch': '<xpath expr="//group[@name=\'group_standard_price\']/label[@for=\'list_price\']" position="attributes"><attribute name="invisible">1</attribute></xpath>'})
            self.env['ir.ui.view'].search([('name', '=', 'product.form.sale.price.inherited')]).write({'arch': '<xpath expr="//group[@name=\'group_standard_price\']/div[@name=\'pricing\']" position="attributes"><attribute name="invisible">1</attribute></xpath> '})
            self.env['ir.ui.view'].search([('name', '=', 'product.purchase.template.form')]).write({'arch':  '''<xpath expr="//page[@name=\'purchase\']" position="inside">
                <field name="seller_ids" invisible="1"/>
                
                <group name="bill" invisible="1">
            <field name="seller_ids" invisible="0">
            <tree>
                        <field name="name" invisible="0"/>
                        <field name="price" invisible="1"/>
                        <field name="currency_id" invisible="1"/>
                        <field name="delay" invisible="0"/>
                    </tree>
                    </field>
        </group>
                </xpath>'''})
            
            self.env['ir.ui.view'].search([('name', '=', 'product.tree.cost.inherited')]).write({'arch': '<xpath expr="//field[@name=\'standard_price\']" position="attributes"><attribute name="invisible">1</attribute></xpath>'})
            self.env['ir.ui.view'].search([('name', '=', 'product.form.cost.price.inherited')]).write({'arch': '<xpath expr="//group[@name=\'group_standard_price\']/label[@for=\'standard_price\']" position="attributes"><attribute name="invisible">1</attribute></xpath>'})
            self.env['ir.ui.view'].search([('name', '=', 'product.form.cost.price.inherited')]).write({'arch': '<xpath expr="//group[@name=\'group_standard_price\']/div[@name=\'standard_price_uom\']" position="attributes"><attribute name="invisible">1</attribute></xpath> '})
