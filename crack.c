#include <stdio.h>  
#include <unistd.h>  
#include <stdlib.h>  
#define _XOPEN_SOURCE  
  
int main(int argc,char * argv[])  
{  
        if (argc != 3){return -1;} 
        char *passwd = crypt((const char *)argv[1],(const char *)argv[2]);  
        printf("%sn",passwd);  
        return 0;  
}
