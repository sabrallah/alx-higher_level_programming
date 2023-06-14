#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

void print_python_bytes(PyObject *p)
{
	long int volum;
	int y;
	char *my_str = NULL;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	PyBytes_AsStringAndSize(p, &my_str, &volum);

	printf("  volum: %li\n", volum);
	printf("  trying string: %s\n", my_str);
	if (volum < 10)
		printf("  first %li bytes:", volum + 1);
	else
		printf("  first 10 bytes:");
	for (y = 0; y <= volum && y < 10; y++)
		printf(" %02hhx", my_str[y]);
	printf("\n");
}

void print_python_list(PyObject *p)
{
        long int volum = PyList_Size(p);
        int y;
        PyListObject *list = (PyListObject *)p;
        const char *type;

        printf("[*] Python list info\n");
        printf("[*] volum of the Python List = %li\n", volum);
        printf("[*] Allocated = %li\n", list->allocated);
        for (y = 0; y < volum; y++)
        {
                type = (list->ob_item[y])->ob_type->tp_name;
		printf("Element %y: %s\n", y, type);
                if (!strcmp(type, "bytes"))
                        print_python_bytes(list->ob_item[y]);
        }
}
