#include <boost/python.hpp>
#include <iostream>

namespace py = boost::python;

void print_helloworld() {
    std::cout << "Hello World" << std::endl;
}

BOOST_PYTHON_MODULE(example1) {
    py::def("print_helloworld", &::print_helloworld);
}
