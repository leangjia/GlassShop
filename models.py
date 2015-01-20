#-*- coding:utf-8 –*-
from openerp import models, fields, api

class GlassShopSaleOrder(models.Model):
    _inherit = 'sale.order'
    #yanguanjilu = fields.One2many('glassshop.yanguanjilu','saleorder','yanguanjilu')
    yanguangjilu = fields.One2many('glassshop.yanguanjilu','saleorder','yanguangjilu')

class GlassShopPartner(models.Model):
    _inherit = 'res.partner'
    yanguanjilu = fields.One2many('glassshop.yanguanjilu','customer','yanguanjilu')

class YanGuanJilu(models.Model):
    _name = 'glassshop.yanguanjilu'

    name = fields.Char(compute='_compute_Name')

    customer = fields.Many2one('res.partner','customer',domain=[('customer','=','1')],required=True)
    date = fields.Date('date',required=True)

    saleorder = fields.Many2one('sale.order','saleorder',required=True)
    yanGuangShi = fields.Many2one('res.partner','yanGuangShi',required=True)
    peiJingShi = fields.Many2one('res.partner','peiJingShi',required=True)

    yongTu = fields.Selection([('jinYong','近用'),('yuanYong','远用')],"用途")
    peiJingLeiXing = fields.Selection([('jingKuang','镜框'),('yinXing','隐形')],"配合类型")

    leftQiuJin= fields.Float('leftQiuJin')
    leftZhuJin= fields.Float('leftZhuJin')
    leftZhouWei= fields.Float('leftZhouWei')
    # leftTongJu= fields.Float('leftTongJu')
    leftTongGao= fields.Float('leftTongGao')
    leftXiaJiaGuang= fields.Float('leftXiaJiaGuang')
    leftJiaoZhengShiLi= fields.Float('leftJiaoZhengShiLi')

    rightQiuJin= fields.Float('rightQiuJin')
    rightZhuJin= fields.Float('rightZhuJin')
    rightZhouWei= fields.Float('rightZhouWei')
    # rightTongJu= fields.Float('rightTongJu')
    rightTongGao= fields.Float('rightTongGao')
    rightXiaJiaGuang= fields.Float('rightXiaJiaGuang')
    rightJiaoZhengShiLi= fields.Float('rightJiaoZhengShiLi')

    zhongTongJu= fields.Float('leftTongJu')
    
    @api.depends('customer','date')
    def _compute_Name(self):
        self.name = '%s @ %s' % (self.customer.display_name,self.date)
        
    # @api.onchange('saleorder')
    # @api.one
    # def _onchange_saleorder(self):
    #         if self.saleorder != None:
    #             self.saleorder.yanguangjilu = self.id
    #         pass
        