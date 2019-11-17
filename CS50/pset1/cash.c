#include <cs50.h>
#include <stdio.h>
#include <math.h>


int main()
{
    float num;
    do
    {
        num = get_float("Change owed: ");
    } 
    while (num < 0);
    
    int int_num = round(num * 100);  /* reduce from decimal */
  
    
    int quarter = int_num / 25;
    int left_quarter = int_num % 25;  /* get remainder */
    
    int dime = left_quarter / 10;
    int left_dime = left_quarter % 10;
    
    int nickel = left_dime / 5;
    int left_nickel = left_dime % 5;
    
    int penny = left_nickel;
    
    /* control situation:
    printf("quarter: %d\n", quarter);
    printf("left_quarter: %d\n", left_quarter);
    
    printf("dime: %d\n", dime);
    printf("left_dime: %d\n", left_dime);
    
    printf("nickel: %d\n", nickel);
    printf("left_nickel: %d\n", left_nickel);
    
    printf("penny: %d\n", penny); */
    
    int total = quarter + dime + nickel + penny;
    
    printf("Total: %d\n", total);
    
    return 0;
}