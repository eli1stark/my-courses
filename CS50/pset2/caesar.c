#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(int argc, string argv[])
{    
    //check argumets, should be only 2
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    
    //convert argument to integer
    int key = atoi(argv[1]);
    
    if (key < 0)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    
    //get text
    string p = get_string("plaintext: ");
    //print out text
    printf("ciphertext: ");
    
    //iterate through plaitext letter by letter
    for (int i = 0, n = strlen(p); i < n; i++)
    {  
        //check if this is uppercase letter
        if (p[i] >= 'A' && p[i] <= 'Z')
        {
            //%26 because in English 26 letters
            //print out uppercase letter
            printf("%c", (((p[i] - 'A') + key) % 26) + 'A');
        }
        //check if this is lowercase letter
        else if (p[i] >= 'a' && p[i] <= 'z')
        {
            //print out lowercase letter
            printf("%c", (((p[i] - 'a') + key) % 26) + 'a');
        }
        //if this symbol(not letter)/
        else
        {
            printf("%c", p[i]);
        }
    }
    printf("\n");
    return 0;
}
