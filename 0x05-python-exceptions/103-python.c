#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - Prints information about a Python list object
 * @p: A pointer to the PyObject representing the Python list
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *item;

	if (!PyList_Check(p))
	{
		printf("[*] Python list info\n");
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	size = PyList_Size(p);

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

/**
 * print_python_bytes - Prints information about a Python bytes object
 * @p: A pointer to the PyObject representing the Python bytes
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *str;

	if (!PyBytes_Check(p))
	{
		printf("[.] bytes object info\n");
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	str = PyBytes_AsString(p);

	printf("[.] bytes object info\n");
	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);

	printf("  first %ld bytes:", size + 1);
	for (i = 0; i <= size; i++)
		printf(" %.2x", (unsigned char)str[i]);
	printf("\n");
}

/**
 * print_python_float - Prints information about a Python float object
 * @p: A pointer to the PyObject representing the Python float
 */
void print_python_float(PyObject *p)
{
	PyObject *repr;

	if (!PyFloat_Check(p))
	{
		printf("[.] float object info\n");
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	repr = PyObject_Repr(p);
	printf("[.] float object info\n");
	printf("  value: %s\n", PyUnicode_AsUTF8(repr));
	Py_DECREF(repr);
}
