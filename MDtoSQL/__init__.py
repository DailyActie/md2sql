# This file is part of md2sql.
# Copyright (C) 2017  Quan Pan
#
# md2sql is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# md2sql is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


"""
__init__
"""


from .SQL import *
from .MD import *
from .ePlatform import ePlatform
from .MDtoSQL import MDtoSQL


__author__ = "Quan Pan"
__version__ = "0.1"
__revision__ = "0.1.1"
__all__ = [
    'SQL',
    'MD',
    'MDtoSQL',
    'ePlatform'
]
