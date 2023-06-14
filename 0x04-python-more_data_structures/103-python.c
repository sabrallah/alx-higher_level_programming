#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

void print_python_bytes(PyObject *p)
{
	long int vol;
	int y;
	char *str = NULL;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	PyBytes_AsStringAndSize(p, &str, &vol);

	printf("  vol: %li\n", vol);
	printf("  trying string: %s\n", str);
	if (vol < 10)
		printf("  first %li bytes:", vol + 1);
	else
		printf("  first 10 bytes:");
	for (y = 0; y <= vol && y < 10; y++)
		printf(" %02hhx", str[y]);
	printf("\n");
}

void print_python_list(PyObject *p)
{
        long int vol = PyList_Size(p);
        int y;
        PyListObject *list = (PyListObject *)p;
        const char *type;

        printf("[*] Python list info\n");
        printf("[*] vol of the Python List = %li\n", vol);
        printf("[*] Allocated = %li\n", list->allocated);
        for (y = 0; y < vol; y++)
        {
                type = (list->ob_item[y])->ob_type->tp_name;
		printf("Element %y: %s\n", y, type);
                if (!strcmp(type, "bytes"))
                        print_python_bytes(list->ob_item[y]);
        }
}
