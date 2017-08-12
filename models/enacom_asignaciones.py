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

from datetime import datetime , timedelta ,  date
from dateutil import parser

from openerp import models, fields, api
from openerp import tools

from openerp.tools.translate import _


import re

class enacom_asignaciones(models.Model):

    _name = "enacom.asignaciones"
    _description = "enacom asignaciones"

    empresa = fields.Char('empresa' , index=True)
    servicio = fields.Char('servicio' , index=True)
    modalidad = fields.Char('modalidad' , index=True)
    localidad = fields.Char('localidad' , index=True)
    indicativo = fields.Integer('indicativo' , index=True)
    bloque = fields.Integer('bloque')

    @api.model
    def get_phone(self,phone_string,filter_modalidad=[]):

        #Esta expresion es a la medida de NQN no de toda argentina
        mob=re.compile('(\+)*(54)*(9)*(0)*(299|291|11|294)*(15)*([4|5|6])([0-9][0-9][0-9][0-9][0-9][0-9])')
        phones=mob.findall(re.sub("\D", "",phone_string))
        for phone in phones:
            indicativo = "299" if  phone[4] == '' else  phone[4]
            number =  str(phone[6])+ str(phone[7])
            bloque1 = number[:3]
            bloque2 = number[:4]

            asignacion = self.search([('indicativo','=',indicativo),('bloque','like',str(bloque1)+'%')],limit=1)
            if asignacion and (filter_modalidad==[]  or asignacion.modalidad in filter_modalidad) :
                return {'indicativo':asignacion.indicativo,
                'modalidad':asignacion.modalidad,
                'servicio':asignacion.servicio,
                'empresa':asignacion.empresa,
                'phone':phone}
            else :
                return False

