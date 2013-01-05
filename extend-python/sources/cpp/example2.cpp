#include <boost/python.hpp>
#include <iostream>
#include <string>

namespace py = boost::python;

class Foo {
public:
    Foo(const std::string &name) {
        this->name = name;
    }

    void say_hello() {
        std::cout << "Hello " << this->name << "!" << std::endl;
    }

private:
    std::string name;
};

BOOST_PYTHON_MODULE(example2) {
    py::class_<Foo>("Foo", py::init<std::string>())
        .def("say_hello", &Foo::say_hello);
}
