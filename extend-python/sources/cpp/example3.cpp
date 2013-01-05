#include <boost/python.hpp>

namespace py = boost::python;

int length1(const py::object &obj) {
    return py::call_method<int>(obj.ptr(), "__len__");
}

int length2(const py::object &obj) {
    return py::extract<int>(obj.attr("__len__")());
}

BOOST_PYTHON_MODULE(example3) {
    py::def("length1", &::length1);
    py::def("length2", &::length2);
}
