#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

//change letter to integer key
int shift(char c)
{
    if (c >= 'A' && c <= 'Z')
    {
        int asc = ((c - 'A') % 26);
        return asc;
    }
    else
    {
        int asc = ((c - 'a') % 26);
        return asc;
    }
}

int main(int argc, string argv[])
{
    //check for arguments
    if (argc != 2)
    {
        printf("./vigenere keyword\n");
        return 1;
    }
    //check for integers
    else 
    {
        for (int i = 0, n = strlen(argv[1]); i < n; i++)
        {
            if (!isalpha(argv[1][i]))
            {
                printf("./vigenere keyword\n");
                return 1;
            }    
        }
    }
    
    //get text
    string p = get_string("plaintext: ");
    //print out text
    printf("ciphertext: ");
    
    int arg_len = strlen(argv[1]);
        
    //iterate through plaitext letter by letter
    for (int i = 0, j = 0, n = strlen(p); i < n; i++)
    {    
        //nulify j when it ends
        if (j == arg_len)
        {
            j = 0;
        }
        int key = shift(argv[1][j]);
        
        //check if this is uppercase letter
        if (p[i] >= 'A' && p[i] <= 'Z')
        {
            //%26 because in English 26 letters
            //print out uppercase letter
            printf("%c", (((p[i] - 'A') + key) % 26) + 'A');
            //go to the next letter key
            j++;
        }
        //check if this is lowercase letter
        else if (p[i] >= 'a' && p[i] <= 'z')
        {
            //print out lowercase letter
            printf("%c", (((p[i] - 'a') + key) % 26) + 'a');
            j++;
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