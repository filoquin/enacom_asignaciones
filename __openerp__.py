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


{
    'name': 'enacom asignaciones',
    'version': '0.1',
    'category': 'parter',
    'description': """
enacom asignaciones
======================


https://www.enacom.gob.ar/asignaciones-a-la-fecha_p445

Numeración geográfica
Es la numeración asociada a una zona geográfica en particular.
Tiene la siguiente estructura: Indicativo Interurbano + Numero de Abonado
El Indicativo Interurbano es el que identifica la zona geográfica a la 
que pertenece el numero de abonado, un ejemplo es el 11 (AMBA) o el 351 (Córdoba),  
el tamaño del indicativo puede ir de 2 a 4 dígitos y como el PFNN establece que 
el numero nacional de abonado tiene que tener 10 dígitos, según sea el tamaño 
del Indicativo, va a ser el tamaño del numero de abonado, que puede tener entre 
6 y 8 dígitos en total.    """,
    'author': 'Hormiga G',
    'website': 'http://www.hormigag.com.ar',
    'depends': ['base'],
    'installable': True,
    'data': ['data/enacom.asignaciones.csv'],
    #'data': [],

    'images':[],    
    'auto_install': False,
}
