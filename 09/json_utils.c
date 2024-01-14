#define PY_SSIZE_T_CLEAN
#include <Python.h>

#include <string.h>
#include <stdio.h>
#include <stdlib.h>


int isJsonObject(const char *jsonStr) {
    int openBraces = 0;
    int closeBraces = 0;
    int colonAfterKey = 0, count_key_values = 0;
    int count = 0;

    if (jsonStr[0] == '{') {
        openBraces = 1;
    }

    for (int i = 0; jsonStr[i] != '\0'; ++i) {
        if (jsonStr[i] == ':') {
            ++colonAfterKey;
        }
        else if (jsonStr[i] == ',') {
            count_key_values += 2;
        }
        ++count;
    }

    count_key_values += 2;

    if (jsonStr[count-1] == '}') {
        closeBraces = 1;
    }

    return openBraces == 1 && closeBraces == 1 && colonAfterKey == (count_key_values/2);
}

int isNumber(const char *str) {
    char *endptr;
    strtod(str, &endptr);
    return *endptr == '\0';
}


PyObject* c_loads(PyObject* self, PyObject* args) {
    const char* jsonStr;

    // парсим аргументы 
    if(!PyArg_ParseTuple(args, "s", &jsonStr)){
        PyErr_Format(PyExc_TypeError, "Invalid argument type");
        return NULL;
    }

    // проверяем является ли строка объектом json
    if(!isJsonObject(jsonStr)) {
        PyErr_Format(PyExc_TypeError, "Expected object or value of json-object");
        return NULL;
    }

    // создаем новый словарь
    PyObject *dict = NULL;
    if (!(dict = PyDict_New())) {
        printf("ERROR: Failed to create Dict Object\n");
        return NULL;
    }

    char key[255];
    char value[255];
    int pos = 1, incr = 0;
    int size = strlen(jsonStr);

    while (sscanf(jsonStr + pos, "\"%[^\":]\": %[^,}]%n", key, value, &incr) == 2 && incr < size - 1) {

        pos += incr +2 ;

        PyObject *pyKey = NULL;
        PyObject *pyValue = NULL;

        if (!(pyKey = Py_BuildValue("s", key))) {
            printf("ERROR: Failed to build string key\n");
            return NULL;
        }

        if (isNumber(value)) {
            if (!(pyValue = Py_BuildValue("i", atoi(value)))) {
                printf("ERROR: Failed to build integer value\n");
                return NULL;
            } 
        } else {
            if (value[0] == '\"') {
                int size_value = strlen(value);
                char result[255]; 
                int len = strlen(value);
                if (len >= 2) { 
                    strncpy(result, value + 1, len - 2); 
                    result[len - 2] = '\0'; 
                }

                if (!(pyValue = Py_BuildValue("s", result))) {
                    printf("ERROR: Failed to build string value\n");
                    return NULL;
                } 
            } else { 
                if (!(pyValue = Py_BuildValue("s", value))) {
                    printf("ERROR: Failed to build string value\n");
                    return NULL;
                }
            }
        }


        if (PyDict_SetItem(dict, pyKey, pyValue) < 0) {
            printf("ERROR: Failed to set item in dict\n");
            return NULL;
        }

    }

    return dict;

}

PyObject* c_dumps(PyObject* self, PyObject* args) {
    PyObject *inputDict;

    // Парсим аргументы
    if (!PyArg_ParseTuple(args, "O", &inputDict)) {
        PyErr_SetString(PyExc_TypeError, "Invalid argument type");
        return NULL;
    }

    // Проверяем, что inputDict действительно является словарем
    if (!PyDict_Check(inputDict)) {
        PyErr_SetString(PyExc_TypeError, "Input must be a dictionary");
        return NULL;
    }


    Py_ssize_t pos = 0;

    PyObject *outputStr = PyUnicode_FromString("{");
    PyObject *key, *value;

    while (PyDict_Next(inputDict, &pos, &key, &value)) {
        PyObject *keyStr = PyObject_Str(key);
        PyObject *valueStr = PyObject_Str(value);

        PyObject *entryStr = PyUnicode_FromFormat("\"%s\": \"%s\", ", PyUnicode_AsUTF8(key), PyUnicode_AsUTF8(value));
        printf("O: %s\n", PyUnicode_AsUTF8(entryStr));

        if (!entryStr) {
            PyErr_SetString(PyExc_MemoryError, "Failed to create entry string");
            Py_XDECREF(keyStr);
            Py_XDECREF(valueStr);
            Py_XDECREF(outputStr);
            return NULL;
        }

        outputStr = PyUnicode_Concat(outputStr, entryStr);
     }

     // Удаляем последнюю запятую и пробел перед закрывающей фигурной скобкой
    Py_ssize_t length = PyUnicode_GET_LENGTH(outputStr);
    Py_UCS1 *str_data = PyUnicode_1BYTE_DATA(outputStr);
    if (length > 2) {
        str_data[length - 2] = '}';
        str_data[length - 1] = '\0';
    } else {
        Py_DECREF(outputStr);
        outputStr = PyUnicode_FromString("{}");
    }
    return outputStr;
}

static PyMethodDef json_utils_methods[] = {
    {"c_loads", c_loads, METH_VARARGS, "Parse JSON string to Python dict"},
    {"c_dumps", c_dumps, METH_VARARGS, "Serialize Python dict to JSON string"},
    {NULL}
 };

static struct PyModuleDef json_utils = {
    PyModuleDef_HEAD_INIT,
    "json_utils",
    NULL,
    -1,
    json_utils_methods
};

PyMODINIT_FUNC PyInit_json_utils(void) {
    return PyModule_Create(&json_utils);
}