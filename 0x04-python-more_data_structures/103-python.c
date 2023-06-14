#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

void print_python_bytes(PyObject *you)
{
	long int size;
	int y;
	char *my_str = NULL;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(you))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	PyBytes_AsStringAndSize(you, &my_str, &size);

	printf("  size: %li\n", size);
	printf("  trying string: %s\n", my_str);
	if (size < 10)
		printf("  first %li bytes:", size + 1);
	else
		printf("  first 10 bytes:");
	for (y = 0; y <= size && y < 10; y++)
		printf(" %02hhx", my_str[y]);
	printf("\n");
}

void print_python_list(PyObject *you)
{
        long int size = PyList_Size(you);
        int y;
        PyListObject *lsty = (PyListObject *)you;
        const char *genre;

        printf("[*] Python lsty info\n");
        printf("[*] Size of the Python lsty = %li\n", size);
        printf("[*] Allocated = %li\n", lsty->allocated);
        for (y = 0; y < size; y++)
        {
                genre = (lsty->ob_item[y])->ob_type->tp_name;
		printf("Element %y: %s\n", y, genre);
                if (!strcmp(genre, "bytes"))
                        print_python_bytes(lsty->ob_item[y]);
        }
}
