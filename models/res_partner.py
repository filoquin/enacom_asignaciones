# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


from openerp import models, fields, api
from openerp import tools

from openerp.tools.translate import _
import logging

_logger = logging.getLogger(__name__)

class res_partner(models.Model):

    _inherit = "res.partner"

    '''
    @api.one
    def write(self,vals):
        res = super(res_partner, self).write(vals)
        _logger.info(vals)

        if 'phone' in vals :
            phone_render = self.env['enacom.asignaciones'].get_phone(vals['phone'])
            _logger.info(phone_render)
    ''' 

    @api.one
    def get_mobile(self,phone_format='{indicativo}{phone[6]}{phone[7]}'):
        
        if self.phone :
            phone_render = self.env['enacom.asignaciones'].get_phone(self.phone,['CPP','MPP'])
            if phone_render :
                return phone_format.format(**phone_render)

        if self.mobile :
            phone_render = self.env['enacom.asignaciones'].get_phone(self.mobile,['CPP','MPP'])
            if phone_render :
                return phone_format.format(**phone_render)
        return False

    @api.one
    def check_phone(self):
        if self.phone :
            phone_render = self.env['enacom.asignaciones'].get_phone(self.phone)
            _logger.info(phone_render)
        
