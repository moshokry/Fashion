###################################################################################
# 
#    Copyright (C) 2019 Fashion  Flixa Logix
#
#    This program is for flixa Logix software: you can redistribute it and/or modify
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
###################################################################################

{
    "name": "Flixa Fashion",
    "summary": """Fashion System""",
    "version": '1.0.0.0.0',
    "category": 'Fashion Management',
    "license": "AGPL-3",
    "website": "http://www.Flixalogix.com",
    "author": "Flixa IT",
    "contributors": [
        "Flixa Team ",
    ],
    "depends": [
        "sale",
    ],
    "data": [
   "views/res_config_settings.xml",
    ],
    "images": [
        'static/description/fl.png'
    ],

       "installable": True,
}