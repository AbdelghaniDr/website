# -*- coding: utf-8 -*-
##############################################################################
#
#     This file is part of website_hr_department, an Odoo module.
#
#     Copyright (c) 2015 ACSONE SA/NV (<http://acsone.eu>)
#     Copyright (c) 2016 Serpent Consulting Services Pvt. Ltd.
#                       (<http://www.serpentcs.com>)
#
#     website_hr_department is free software: you can redistribute it and/or
#     modify it under the terms of the GNU Affero General Public License
#     as published by the Free Software Foundation, either version 3 of
#     the License, or (at your option) any later version.
#
#     website_hr_department is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU Affero General Public License for more details.
#
#     You should have received a copy of the
#     GNU Affero General Public License
#     along with website_hr_department.
#     If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': "Departments Page",
    'summary': """
        Display the structure of your departments and their members.
        """,
    'author': "ACSONE SA/NV, "
              "Odoo Community Association (OCA), "
              "Serpent Consulting Services Pvt. Ltd. ",
             
    'website': "http://acsone.eu, http://www.serpentcs.com",
    'category': 'Website',
    'version': '9.0.1.0.0',
    'license': 'AGPL-3',
    'depends': [
        'website_hr',
    ],
    'data': [
        'security/ir.model.access.csv',
        'security/website_hr_department.xml',
        'data/websiste_hr_department_data.xml',
        'views/website_hr_department.xml',
    ],
    'installable': True,
}
