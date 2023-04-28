/*###########################################################################
# Copyright (C) 2023 CrowdWare
#
# This file is part of AzerothClient.
#
#  AzerothClient is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  AzerothClient is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with AzerothClient.  If not, see <http://www.gnu.org/licenses/>.
#
###########################################################################*/
#include <pybind11/pybind11.h>
#include "../lib/mymath.h"

#define STRINGIFY(x) #x
#define MACRO_STRINGIFY(x) STRINGIFY(x)


namespace py = pybind11;

PYBIND11_MODULE(azerothlib, m) 
{
    m.doc() = R"pbdoc(
        Pybind11 binding for AzerothCore
        --------------------------------

        .. currentmodule:: azerothcore

        .. autosummary::
           :toctree: _generate

           add
           sub
    )pbdoc";

    m.def("add", &add, R"pbdoc(
        Add two numbers

        Some other explanation about the add function.
    )pbdoc");

    m.def("sub", &sub, R"pbdoc(
        Subtract number from numer

        Some other explanation about the sub function.
    )pbdoc");

    m.attr("__version__") = "0.0.2";
}
