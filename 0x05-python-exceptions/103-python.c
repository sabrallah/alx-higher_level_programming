#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Prints basic info about Python lists.
 * @p: A PyObject my_list object.
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t my_size, my_alloc, y;
	const char *my_type;
	PyListObject *my_list = (PyListObject *)p;
	PyVarObject *my_var = (PyVarObject *)p;

	my_size = my_var->ob_size;
	my_alloc = my_list->allocated;

	fflush(stdout);

	printf("[*] Python my_list info\n");
	if (strcmp(p->ob_type->tp_name, "my_list") != 0)
	{
		printf("  [ERROR] Invalid my_list Object\n");
		return;
	}

	printf("[*] my_size of the Python my_list = %ld\n", my_size);
	printf("[*] Allocated = %ld\n", my_alloc);

	for (y = 0; y < my_size; y++)
	{
		my_type = my_list->ob_item[y]->ob_type->tp_name;
		printf("Element %ld: %s\n", y, my_type);
		if (strcmp(my_type, "bytes") == 0)
			print_python_bytes(my_list->ob_item[y]);
		else if (strcmp(my_type, "float") == 0)
			print_python_float(my_list->ob_item[y]);
	}
}

/**
 * print_python_bytes - Prints basic info about Python byte objects.
 * @p: A PyObject byte object.
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t my_size, y;
	PyBytesObject *bytes = (PyBytesObject *)p;

	fflush(stdout);

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  my_size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (((PyVarObject *)p)->ob_size >= 10)
		my_size = 10;
	else
		my_size = ((PyVarObject *)p)->ob_size + 1;

	printf("  first %ld bytes: ", my_size);
	for (y = 0; y < my_size; y++)
	{
		printf("%02hhx", bytes->ob_sval[y]);
		if (y == (my_size - 1))
			printf("\n");
		else
			printf(" ");
	}
}

/**
 * print_python_float - Prints basic info about Python float objects.
 * @p: A PyObject float object.
 */
void print_python_float(PyObject *p)
{
	char *buffer = NULL;

	PyFloatObject *float_obj = (PyFloatObject *)p;

	fflush(stdout);

	printf("[.] float object info\n");
	if (strcmp(p->ob_type->tp_name, "float") != 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	buffer = PyOS_double_to_string(float_obj->ob_fval, 'r', 0,
			Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", buffer);
	PyMem_Free(buffer);
}
