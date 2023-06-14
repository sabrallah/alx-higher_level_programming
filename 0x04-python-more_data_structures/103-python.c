#include <stdio.h>
#include <Python.h>

/**
 * print_bytes_info - Prints bytes information
 *
 * @py_obj: Python Object
 * Return: no return
 */
void print_bytes_info(PyObject *py_obj)
{
	char *str;
	long int sz, idx, lim;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(py_obj))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	sz = ((PyVarObject *)(py_obj))->ob_size;
	str = ((PyBytesObject *)py_obj)->ob_sval;

	printf("  size: %ld\n", sz);
	printf("  trying string: %s\n", str);

	if (sz >= 10)
		lim = 10;
	else
		lim = sz + 1;

	printf("  first %ld bytes:", lim);

	for (idx = 0; idx < lim; idx++)
		if (str[idx] >= 0)
			printf(" %02x", str[idx]);
		else
			printf(" %02x", 256 + str[idx]);

	printf("\n");
}

/**
 * print_list_info - Prints list information
 *
 * @py_obj: Python Object
 * Return: no return
 */
void print_list_info(PyObject *py_obj)
{
	long int sz, idx;
	PyListObject *lst;
	PyObject *obj;

	sz = ((PyVarObject *)(py_obj))->ob_size;
	lst = (PyListObject *)py_obj;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", sz);
	printf("[*] Allocated = %ld\n", lst->allocated);

	for (idx = 0; idx < sz; idx++)
	{
		obj = ((PyListObject *)py_obj)->ob_item[idx];
		printf("Element %ld: %s\n", idx, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_bytes_info(obj);
	}
}
