#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

void print_python_bytes(PyObject *p)
{
    PyBytesObject *bytes = (PyBytesObject *)p;
    long int size;
    int i;

    printf("[.] bytes object info\n");

    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    char *trying_str = PyBytes_AsString(p);

    printf("  size: %li\n", size);
    printf("  trying string: %s\n", trying_str);

    if (size < 10)
        printf("  first %li bytes:", size + 1);
    else
        printf("  first 10 bytes:");

    for (i = 0; i <= size && i < 10; i++)
        printf(" %02hhx", trying_str[i]);

    printf("\n");
}

void print_python_list(PyObject *p)
{
    PyListObject *list = (PyListObject *)p;
    long int size = PyList_Size(p);
    int i;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %li\n", size);
    printf("[*] Allocated = %li\n", list->allocated);

    for (i = 0; i < size; i++)
    {
        PyObject *item = list->ob_item[i];
        const char *type = Py_TYPE(item)->tp_name;

        printf("Element %i: %s\n", i, type);

        if (strcmp(type, "bytes") == 0)
            print_python_bytes(item);
    }
}
