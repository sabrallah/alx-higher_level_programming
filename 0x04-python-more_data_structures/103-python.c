#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - Prints bytes information
 *
 * @you: Python Object
 * Return: no return
 */
void print_python_bytes(PyObject *you)
{
	char *str;
	long int size, y, max;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(you))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)(you))->ob_size;
	str = ((PyBytesObject *)you)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying str: %s\n", str);

	if (size >= 10)
		max = 10;
	else
		max = size + 1;

	printf("  first %ld bytes:", max);

	for (y = 0; y < max; y++)
		if (str[y] >= 0)
			printf(" %02x", str[y]);
		else
			printf(" %02x", 256 + str[y]);

	printf("\n");
}

/**
 * print_python_list - Prints li information
 *
 * @you: Python Object
 * Return: no return
 */
void print_python_list(PyObject *you)
{
	long int size, y;
	PyListObject *li;
	PyObject *object;

	size = ((PyVarObject *)(you))->ob_size;
	li = (PyListObject *)you;

	printf("[*] Python li info\n");
	printf("[*] Size of the Python li = %ld\n", size);
	printf("[*] Allocated = %ld\n", li->allocated);

	for (y = 0; y < size; y++)
	{
		object = ((PyListObject *)you)->ob_item[y];
		printf("Element %ld: %s\n", y, ((object)->ob_type)->tp_name);
		if (PyBytes_Check(object))
			print_python_bytes(object);
	}
