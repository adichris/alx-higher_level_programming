#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p)
{
	Py_ssize_t size = PyList_Size(p);

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (int i = 0; i < size && i < 5; i++)
	{
		PyObject *item = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(item)->tp_name);
	}
}

void print_python_bytes(PyObject *p)
{
	if (!PyBytes_Check(p))
	{
		printf("[ERROR] Invalid Bytes Object\n");
		return;
	}

	Py_ssize_t size = PyBytes_Size(p);

	printf("[*] Python bytes info\n");
	printf("[*] Size = %ld\n", size);
	printf("[*] Trying string: %s\n", PyBytes_AsString(p));
	printf("First 10 bytes: ");

	for (int i = 0; i < 10 && i < size; i++)
	{
		printf("%02x ", PyBytes_AS_STRING(p)[i]);
	}

	printf("\n");
}