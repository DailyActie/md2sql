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
MD
"""


import markdown


class MD(object):
    """MD
    """

    def __init__(self):
        # super(MD, self).__init__()

        self.md = markdown

    def toHTML(self):
        """
        Description
        :param arg:
        :return:

        """
        # import codecs
        # input_file = codecs.open("w.vanhage.md", mode="r", encoding="utf-8")
        # text = input_file.read()
        # html = self.md.markdown(text)

        self.md.markdownFromFile(input="data_md/person-template.md",output="data_md/person.html",encoding="utf-8")
        self.md.markdownFromFile(input="data_md/w.vanhage.md",output="data_md/w.vanhage.html",encoding="utf-8")
