#include <stdio.h>

#include <string.h>

 

int main(void){

        char key[1024] = "28714143kkl23jlsdkj34hji53jhk345khj543jhk354h354jh354jhkl354jhkl354hjk345hjk3h4i5h3l4h5iul34u6h4e5uh7ui5h7uilyhhiuyhuileyhlui6yhuilyuhil55hhuilhiw543uhiw34uhihuiuh6iwl354h";

 

        char buffer[34] = {0x76, 0x34,0x71,0x76,0x4f,0x4c,0x7b,0x42,0x0e,0x5e,0x06,0x4e,0x02,0x72,0x50,0x01,0x53,0x07,0x0c,0x34,0x06,0x4b,0x07,0x04,0x2a,0x61,0x0a,0x66,0x73,0x53,0x03,0x4e,0x04,0x00};

 

        int v5 = atoi(key);

        int v0 = 0, v6 = 0, v1 = 0, v3 = 0,i,j;

        char v7;

        char output[1024];

 

        v1 = key;

 

        for(i =256; i; --i){

        v1 = 0;

        v1 += 4;}

 

        v3 = output;

 

        for(j = 256; j; --j){

        v3 = 0;

        v3 += 4;

        }

 

        sprintf(key, "0x%08x", v5);

 

        while(v0 < strlen(buffer)){

        v7 = key[v6++];

        sprintf(output,"%s%c",output, v7^buffer[v0]);

        if(v6 == strlen(key)){v6 = 0;}

        ++v0;

    }

        printf("<1>%s\n",output);

        return 0;

}


