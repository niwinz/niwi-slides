#include <stdio.h>
#include <Python.h>

/*
 * Example passing python obj pointer
*/

void print_address(PyObject *obj) {
    PyObject *func, *res;

    func = PyObject_GetAttrString(obj, "get_address");
    res = PyObject_CallFunction(func, NULL);

    char *result = PyUnicode_AsUTF8(PyObject_Str(res));
    printf("Result: %s\n", result);

    Py_DECREF(res);
    Py_DECREF(func);
}
