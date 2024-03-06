#include <stdio.h>

#ifdef __cplusplus
extern "C" {
#endif

void call_me()
{
    printf( "Hello from C land.\n" );
}

#ifdef __cplusplus
}
#endif
