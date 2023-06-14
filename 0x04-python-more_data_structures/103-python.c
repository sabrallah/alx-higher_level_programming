#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

void print_python_bytes(PyObject *p)
{
    long int byteSize;
    int i;
    char *byteString = NULL;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    PyBytes_AsStringAndSize(p, &byteString, &byteSize);

    printf("  size: %li\n", byteSize);
    printf("  byte string: %s\n", byteString);
    if (byteSize < 10)
        printf("  first %li bytes:", byteSize + 1);
    else
        printf("  first 10 bytes:");
    for (i = 0; i <= byteSize && i < 10; i++)
        printf(" %02hhx", byteString[i]);
    printf("\n");
}

void print_python_list(PyObject *p)
{
    long int list_size = PyList_Size(p);
    int index;
    PyListObject *list_obj = (PyListObject *)p;
    const char *element_type;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %li\n", list_size);
    printf("[*] Allocated = %li\n", list_obj->allocated);

    for (index = 0; index < list_size; index++)
    {
        element_type = (list_obj->ob_item[index])->ob_type->tp_name;
        printf("Element %i: %s\n", index, element_type);
        if (!strcmp(element_type, "bytes"))
            print_python_bytes(list_obj->ob_item[index]);
    }
}
