#include <stdio.h>
#include <Python.h>

#ifdef __cplusplus
extern "C" {
#endif

PyMODINIT_FUNC PyInit_my_extension(void) {
    return NULL; // or PyModule_Create(&module_definition); if you have a module definition
}

void call_me()
{
    printf( "Hello from C land.\n" );
}

#ifdef __cplusplus
}
#endif
