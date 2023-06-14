#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

void print_python_bytes(PyObject *bytes_object)
{
    long int size;
    int i;
    char *string_value = NULL;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(bytes_object))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    PyBytes_AsStringAndSize(bytes_object, &string_value, &size);

    printf("  size: %li\n", size);
    printf("  string value: %s\n", string_value);
    if (size < 10)
        printf("  first %li bytes:", size + 1);
    else
        printf("  first 10 bytes:");
    for (i = 0; i <= size && i < 10; i++)
        printf(" %02hhx", string_value[i]);
    printf("\n");
}

void print_python_list(PyObject *list_object)
{
    long int size = PyList_Size(list_object);
    int i;
    PyListObject *list = (PyListObject *)list_object;
    const char *type_name;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %li\n", size);
    printf("[*] Allocated = %li\n", list->allocated);
    for (i = 0; i < size; i++)
    {
        type_name = (list->ob_item[i])->ob_type->tp_name;
        printf("Element %i: %s\n", i, type_name);
        if (!strcmp(type_name, "bytes"))
            print_python_bytes(list->ob_item[i]);
    }
}

