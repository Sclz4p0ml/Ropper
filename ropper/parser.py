# coding=utf-8
#
# Copyright 2017 Sascha Schirra
#
# This file is part of Ropper.
#
# Ropper is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ropper is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

class ExpressionCompiler(object):
    """
    Compile a user given constraints to z3 expressions

    constraint := assignment | pop_reg
    assignment := reg, adjust, reg | number
    pop_reg := "pop", reg
    adjust := "==" | "+=" | "-=" | "*=" | "/="
    reg := a register of the current architecture
    number := int
    """

    ASSIGNMENT = '([a-zA-Z0-9]+) +?([\\+\-\*/=]=) +?(\[?)(\-?[a-zA-Z0-9]+)(\]?)'

    def parse(self, line):
        """
        parse a line of semantic expressions
        """
        insts = line.split(';')

    def tokenize(self, line):
        pass
