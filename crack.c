#include <stdio.h>  
#include <unistd.h>
#include <string.h>
#include <crypt.h>
#include <stdlib.h>  
//#define _XOPEN_SOURCE  
  
int main(int argc,char * argv[])  
{  
        if (argc != 3){return -1;} 
        //char *passwd = crypt((const char *)argv[1],(const char *)argv[2]);  
        printf("%s\n",crypt((const char *)argv[1],(const char *)argv[2]););  
        return 0;  
}
