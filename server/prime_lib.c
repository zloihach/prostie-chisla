#include <Python.h>
#include <stdlib.h>

// Проверка простоты числа
static PyObject* is_prime(PyObject* self, PyObject* args) {
    int n;
    if (!PyArg_ParseTuple(args, "i", &n)) {
        return NULL;
    }
    if (n <= 1) return Py_BuildValue("O", Py_False);
    if (n == 2) return Py_BuildValue("O", Py_True);
    if (n % 2 == 0) return Py_BuildValue("O", Py_False);
    for (int i = 3; i * i <= n; i += 2) {
        if (n % i == 0) return Py_BuildValue("O", Py_False);
    }
    return Py_BuildValue("O", Py_True);
}

// Решето Эратосфена
static PyObject* sieve_of_eratosthenes(PyObject* self, PyObject* args) {
    int limit;
    if (!PyArg_ParseTuple(args, "i", &limit)) {
        return NULL;
    }

    int* sieve = (int*)malloc((limit + 1) * sizeof(int));
    for (int i = 0; i <= limit; i++) sieve[i] = 1;
    sieve[0] = sieve[1] = 0;

    for (int p = 2; p * p <= limit; p++) {
        if (sieve[p] == 1) {
            for (int i = p * p; i <= limit; i += p) {
                sieve[i] = 0;
            }
        }
    }

    PyObject* prime_list = PyList_New(0);
    for (int i = 2; i <= limit; i++) {
        if (sieve[i] == 1) {
            PyList_Append(prime_list, PyLong_FromLong(i));
        }
    }

    free(sieve);
    return prime_list;
}

// N-е простое число
static PyObject* nth_prime(PyObject* self, PyObject* args) {
    int n, count = 0, num = 1;
    if (!PyArg_ParseTuple(args, "i", &n)) {
        return NULL;
    }

    while (count < n) {
        num += 1;
        if (num == 2 || (num % 2 != 0 && PyObject_IsTrue(is_prime(self, Py_BuildValue("(i)", num))))) {
            count += 1;
        }
    }

    return Py_BuildValue("i", num);
}

// Простая факторизация
static PyObject* prime_factors(PyObject* self, PyObject* args) {
    int n;
    if (!PyArg_ParseTuple(args, "i", &n)) {
        return NULL;
    }

    PyObject* factor_list = PyList_New(0);

    while (n % 2 == 0) {
        PyList_Append(factor_list, PyLong_FromLong(2));
        n /= 2;
    }

    for (int i = 3; i * i <= n; i += 2) {
        while (n % i == 0) {
            PyList_Append(factor_list, PyLong_FromLong(i));
            n /= i;
        }
    }

    if (n > 2) {
        PyList_Append(factor_list, PyLong_FromLong(n));
    }

    return factor_list;
}

// Методы библиотеки
static PyMethodDef PrimeMethods[] = {
    {"is_prime", is_prime, METH_VARARGS, "Check if a number is prime."},
    {"sieve_of_eratosthenes", sieve_of_eratosthenes, METH_VARARGS, "Generate primes up to a limit using the Sieve of Eratosthenes."},
    {"nth_prime", nth_prime, METH_VARARGS, "Get the nth prime number."},
    {"prime_factors", prime_factors, METH_VARARGS, "Get prime factors of a number."},
    {NULL, NULL, 0, NULL}
};

// Определение модуля
static struct PyModuleDef prime_module = {
    PyModuleDef_HEAD_INIT,
    "prime_lib",
    NULL,
    -1,
    PrimeMethods
};

// Инициализация модуля
PyMODINIT_FUNC PyInit_prime_lib(void) {
    return PyModule_Create(&prime_module);
}
