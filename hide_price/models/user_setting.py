from odoo import fields, models, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    qty_available = fields.Float(string='Quantity Available')
    name = fields.Char(required=False)

    



class UserExtension(models.Model):
    _inherit = 'res.users'

    # cost_price = fields.Boolean(string="Show Cost Price")
    # sale_price = fields.Boolean(string="Show Sale Price")
    # show_sale_price = fields.Boolean(string="Show Sale Price", compute='_compute_show_sale_price', store=True)

    # @api.model
    # def get_cost_price(self):
    #     return True


    # @api.onchange('')
    # def _update_sale_price_views(self):
    #     users = self.search([])
    #     for user in users:
    #         if user.sale_price:
    #             # Perform action when sale_price is True
    #             self._action_when_sale_price_checked(user)
    #         else:
    #             # Perform action when sale_price is False
    #             self._action_when_sale_price_unchecked(user)

    # def _action_when_sale_price_checked(self, user):
    #      user.env['ir.ui.view'].search([('name', '=', 'kanban_sale_price')]).write({'arch': '<xpath expr="//div[@name=\'product_lst_price\']" position="attributes"><attribute name="invisible">0</attribute></xpath>'})


    # def _action_when_sale_price_unchecked(self, user):
    #     user.env['ir.ui.view'].search([('name', '=', 'kanban_sale_price')]).write({'arch': '<xpath expr="//div[@name=\'product_lst_price\']" position="attributes"><attribute name="invisible">1</attribute></xpath>'})


    

       

    

    # @api.onchange('sale_price')
    # def _onchange_sale_price(self):
    #    for user in self:
    #         if user.sale_price:
    #     #         # print(self.env.user)


                    
    #             # kanban view
            #  user.env['ir.ui.view'].search([('name', '=', 'kanban_sale_price')]).write({'arch': '<xpath expr="//div[@name=\'product_lst_price\']" position="attributes"><attribute name="invisible">0</attribute></xpath>'})
    #                 # form view
    #         self.env['ir.ui.view'].search([('name', '=', 'product.tax.string.prices')]).write({'arch': '<xpath expr="//div[@name=\'pricing\']" position="attributes"><attribute name="style"></attribute></xpath>'})
    #         self.env['ir.ui.view'].search([('name', '=', 'product.form.sale.prices.inherited')]).write({'arch': '<xpath expr="//field[@name=\'list_price\']" position="attributes"><attribute name="invisible">0</attribute></xpath>'})
    #             # tree view
    #         self.env['ir.ui.view'].search([('name', '=', 'product.tree.sale.inherited')]).write({'arch': '<xpath expr="//field[@name=\'list_price\']" position="attributes"><attribute name="invisible">0</attribute></xpath>'})
                # variant kanban 
            # user.env['ir.ui.view'].search([('name', '=', 'product.variant.kanban.inherited')]).write({'arch': '<xpath expr="//ul/li/strong[field/@name=\'lst_price\']" position="attributes"><attribute name="invisible">0</attribute></xpath>'})
            #     # variant tree
            #     user.env['ir.ui.view'].search([('name', '=', 'product_variant_sale_tree')]).write({'arch': '<xpath expr="//field[@name=\'lst_price\']" position="attributes"><attribute name="invisible">0</attribute></xpath>'})
            #     # purchase tree
            #     user.env['ir.ui.view'].search([('name', '=', 'product.purchase.template.form')]).write({'arch': '''<xpath expr="//page[@name=\'purchase\']" position="inside">
            #                 <field name="seller_ids" invisible="1"/>
                            
            #                 <group name="bill" invisible="1">
            #                 <field name="seller_ids" invisible="0">
            #                     <tree>
            #                             <field name="partner_id" invisible="0"/>
            #                             <field name="price" invisible="0"/>
            #                             <field name="currency_id" invisible="0"/>
            #                             <field name="delay" invisible="0"/>
            #                     </tree>
            #                     </field>
            #                 </group>
            #                 </xpath>'''
            #             })

            # if not user.sale_price :         
        #         # kanban view
        #         print(self.env.user)

                # self.env['ir.ui.view'].search([('name', '=', 'kanban_sale_price')]).write({'arch': '<xpath expr="//div[@name=\'product_lst_price\']" position="attributes"><attribute name="invisible">1</attribute></xpath>'})
        #         # form view
                # self.env['ir.ui.view'].search([('name', '=', 'product.tax.string.prices')]).write({'arch': '<xpath expr="//div[@name=\'pricing\']" position="attributes"><attribute name="style">display:none;</attribute></xpath>'})
                # self.env['ir.ui.view'].search([('name', '=', 'product.form.sale.prices.inherited')]).write({'arch': '<xpath expr="//field[@name=\'list_price\']" position="attributes"><attribute name="invisible">1</attribute></xpath>'})
                # return            
                        # tree view 
                # user.env['ir.ui.view'].search([('name', '=', 'product.tree.sale.inherited')]).write({'arch': '<xpath expr="//field[@name=\'list_price\']" position="attributes"><attribute name="invisible">1</attribute></xpath>'})
                #     # variant kanban
                # user.env['ir.ui.view'].search([('name', '=', 'product.variant.kanban.inherited')]).write({'arch': '<xpath expr="//ul/li/strong[field/@name=\'lst_price\']" position="attributes"><attribute name="invisible">1</attribute></xpath>'})
                #     # variant tree
                # user.env['ir.ui.view'].search([('name', '=', 'product_variant_sale_tree')]).write({'arch': '<xpath expr="//field[@name=\'lst_price\']" position="attributes"><attribute name="invisible">1</attribute></xpath>'})
                #     # purchase tree
                # user.env['ir.ui.view'].search([('name', '=', 'product.purchase.template.form')]).write({'arch': '''<xpath expr="//page[@name=\'purchase\']" position="inside">
                #         <field name="seller_ids" invisible="1"/>
                        
                #         <group name="bill" invisible="1">
                #         <field name="seller_ids" invisible="0">
                #             <tree>
                #                     <field name="partner_id" invisible="0"/>
                #                     <field name="price" invisible="1"/>
                #                     <field name="currency_id" invisible="1"/>
                #                     <field name="delay" invisible="0"/>
                #             </tree>
                #             </field>
                #         </group>
                #         </xpath>'''
                #     })
            
    
            # if user.cost_price:
    #             # form view
    #             user.env['ir.ui.view'].search([('name', '=', 'product.form.cost.prices.inherited')]).write({'arch': '<xpath expr="//field[@name=\'standard_price\']" position="attributes"><attribute name="invisible">0</attribute></xpath>'})
    # #             # tree view
    #             user.env['ir.ui.view'].search([('name', '=', 'product.tree.cost.inherited')]).write({'arch': '<xpath expr="//field[@name=\'standard_price\']" position="attributes"><attribute name="invisible">0</attribute></xpath>'})
    # #             # variant tree view
    #             user.env['ir.ui.view'].search([('name', '=', 'product_variant_cost_tree')]).write({'arch': '<xpath expr="//field[@name=\'standard_price\']" position="attributes"><attribute name="invisible">0</attribute></xpath>'})


    #         if not user.cost_price:
    #             # form view
    #             user.env['ir.ui.view'].search([('name', '=', 'product.form.cost.prices.inherited')]).write({'arch': '<xpath expr="//field[@name=\'standard_price\']" position="attributes"><attribute name="invisible">1</attribute></xpath>'})
    # #             # tree view 
    #             user.env['ir.ui.view'].search([('name', '=', 'product.tree.cost.inherited')]).write({'arch': '<xpath expr="//field[@name=\'standard_price\']" position="attributes"><attribute name="invisible">1</attribute></xpath>'})
    # #             # variant tree view 
    #             user.env['ir.ui.view'].search([('name', '=', 'product_variant_cost_tree')]).write({'arch': '<xpath expr="//field[@name=\'standard_price\']" position="attributes"><attribute name="invisible">1</attribute></xpath>'})


    # @api.onchange('cost_price')
    # def _onchange_cost_price(self):
    #     for user in self:
    #         if user.cost_price:
    #             # form view
    #             user.env['ir.ui.view'].search([('name', '=', 'product.form.cost.prices.inherited')]).write({'arch': '<xpath expr="//field[@name=\'standard_price\']" position="attributes"><attribute name="invisible">0</attribute></xpath>'})
    #             # tree view
    #             user.env['ir.ui.view'].search([('name', '=', 'product.tree.cost.inherited')]).write({'arch': '<xpath expr="//field[@name=\'standard_price\']" position="attributes"><attribute name="invisible">0</attribute></xpath>'})
    #             # variant tree view
    #             user.env['ir.ui.view'].search([('name', '=', 'product_variant_cost_tree')]).write({'arch': '<xpath expr="//field[@name=\'standard_price\']" position="attributes"><attribute name="invisible">0</attribute></xpath>'})

       
       
    #         else:

    #             # form view
    #             user.env['ir.ui.view'].search([('name', '=', 'product.form.cost.prices.inherited')]).write({'arch': '<xpath expr="//field[@name=\'standard_price\']" position="attributes"><attribute name="invisible">1</attribute></xpath>'})
    #             # tree view 
    #             user.env['ir.ui.view'].search([('name', '=', 'product.tree.cost.inherited')]).write({'arch': '<xpath expr="//field[@name=\'standard_price\']" position="attributes"><attribute name="invisible">1</attribute></xpath>'})
    #             # variant tree view 
    #             user.env['ir.ui.view'].search([('name', '=', 'product_variant_cost_tree')]).write({'arch': '<xpath expr="//field[@name=\'standard_price\']" position="attributes"><attribute name="invisible">1</attribute></xpath>'})
        
