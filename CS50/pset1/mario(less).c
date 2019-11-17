#include <cs50.h>
#include <stdio.h>

int main() 
{
    int num;
    printf("Height: ");
    scanf("%d", &num);  
    
    while (num < 1 || num > 8) 
    {
        printf("Height: ");
        scanf("%d", &num);  
    }
    
    if (num == 1)
    {
        printf("#\n");
    }
    if (num == 2)
    {
        printf(" #\n");
        printf("##\n");
    }
    if (num == 3)
    {
        printf("  #\n");
        printf(" ##\n");
        printf("###\n");
    }
    if (num == 4)
    {
        printf("   #\n");
        printf("  ##\n");
        printf(" ###\n");
        printf("####\n");
    }
    if (num == 5)
    {
        printf("    #\n");
        printf("   ##\n");
        printf("  ###\n");
        printf(" ####\n");
        printf("#####\n");
    }
    if (num == 6)
    {
        printf("     #\n");
        printf("    ##\n");
        printf("   ###\n");
        printf("  ####\n");
        printf(" #####\n");
        printf("######\n");
    }
    if (num == 7)
    {
        printf("      #\n");
        printf("     ##\n");
        printf("    ###\n");
        printf("   ####\n");
        printf("  #####\n");
        printf(" ######\n");
        printf("#######\n");
    }
    if (num == 8)
    {
        printf("       #\n");
        printf("      ##\n");
        printf("     ###\n");
        printf("    ####\n");
        printf("   #####\n");
        printf("  ######\n");
        printf(" #######\n");
        printf("########\n");
    }
    
    
    
    return 0;
}