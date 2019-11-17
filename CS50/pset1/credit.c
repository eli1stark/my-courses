#include <cs50.h>
#include <stdio.h>

int main()
{
    long card;
    do
    {
        card = get_long("Number: ");
    }
    while (card < 0);
    
    //decompose number:
    int num_16 = card % 10;
    int num_15 = (card / 10) % 10;
    int num_14 = (card / 100) % 10;
    int num_13 = (card / 1000) % 10;
    int num_12 = (card / 10000) % 10;
    int num_11 = (card / 100000) % 10;
    int num_10 = (card / 1000000) % 10;
    int num_9 = (card / 10000000) % 10;
    int num_8 = (card / 100000000) % 10;
    int num_7 = (card / 1000000000) % 10;
    int num_6 = (card / 10000000000) % 10;
    int num_5 = (card / 100000000000) % 10;
    int num_4 = (card / 1000000000000) % 10;
    int num_3 = (card / 10000000000000) % 10;
    int num_2 = (card / 100000000000000) % 10;
    int num_1 = (card / 1000000000000000) % 10;
    
    //odd_sum = num_15, num_13, num_11, num_9, num_7, num_5, num_3, num_1;
    //double odd numbers:
    int odd_dub_15 = num_15 * 2;
    int odd_dub_13 = num_13 * 2;
    int odd_dub_11 = num_11 * 2;
    int odd_dub_9 = num_9 * 2;
    int odd_dub_7 = num_7 * 2;
    int odd_dub_5 = num_5 * 2;
    int odd_dub_3 = num_3 * 2;
    int odd_dub_1 = num_1 * 2;
   
    //declare sum:
    int odd_sum_15;
    int odd_sum_13;
    int odd_sum_11;
    int odd_sum_9;
    int odd_sum_7;
    int odd_sum_5;
    int odd_sum_3;
    int odd_sum_1;
    
    //Conditions for odd numbers:
    if (odd_dub_15 > 9)
    {
        int odd_dub_15_1 = odd_dub_15 % 10;
        int odd_dub_15_2 = (odd_dub_15 / 10) % 10; 
        odd_sum_15 = odd_dub_15_1 + odd_dub_15_2;
    }
    else 
    {
        odd_sum_15 = odd_dub_15;
    }
   
    if (odd_dub_13 > 9)
    {
        int odd_dub_13_1 = odd_dub_13 % 10;
        int odd_dub_13_2 = (odd_dub_13 / 10) % 10; 
        odd_sum_13 = odd_dub_13_1 + odd_dub_13_2;
    }
    else 
    {
        odd_sum_13 = odd_dub_13;
    }
   
    if (odd_dub_11 > 9)
    {
        int odd_dub_11_1 = odd_dub_11 % 10;
        int odd_dub_11_2 = (odd_dub_11 / 10) % 10; 
        odd_sum_11 = odd_dub_11_1 + odd_dub_11_2;
    }
    else 
    {
        odd_sum_11 = odd_dub_11;
    }
    
    if (odd_dub_9 > 9)
    {
        int odd_dub_9_1 = odd_dub_9 % 10;
        int odd_dub_9_2 = (odd_dub_9 / 10) % 10; 
        odd_sum_9 = odd_dub_9_1 + odd_dub_9_2;
    }
    else 
    {
        odd_sum_9 = odd_dub_9;
    }
    
    if (odd_dub_7 > 9)
    {
        int odd_dub_7_1 = odd_dub_7 % 10;
        int odd_dub_7_2 = (odd_dub_7 / 10) % 10; 
        odd_sum_7 = odd_dub_7_1 + odd_dub_7_2;
    }
    else 
    {
        odd_sum_7 = odd_dub_7;
    }
    
    if (odd_dub_5 > 9)
    {
        int odd_dub_5_1 = odd_dub_5 % 10;
        int odd_dub_5_2 = (odd_dub_5 / 10) % 10; 
        odd_sum_5 = odd_dub_5_1 + odd_dub_5_2;
    }
    else 
    {
        odd_sum_5 = odd_dub_5;
    }
    
    if (odd_dub_3 > 9)
    {
        int odd_dub_3_1 = odd_dub_3 % 10;
        int odd_dub_3_2 = (odd_dub_3 / 10) % 10; 
        odd_sum_3 = odd_dub_3_1 + odd_dub_3_2;
    }
    else 
    {
        odd_sum_3 = odd_dub_3;
    }
    
    if (odd_dub_1 > 9)
    {
        int odd_dub_1_1 = odd_dub_1 % 10;
        int odd_dub_1_2 = (odd_dub_1 / 10) % 10; 
        odd_sum_1 = odd_dub_1_1 + odd_dub_1_2;
    }
    else 
    {
        odd_sum_1 = odd_dub_1;
    }
    //add odd numbers for VISA/MASTERCARD/INVALID:
    int odd_all_sum = odd_sum_15 + odd_sum_13 + odd_sum_11 + odd_sum_9 + odd_sum_7 + odd_sum_5 + odd_sum_3 + odd_sum_1;
        
    //add all numbers for VISA/MASTERCARD/INVALID:
    int all_sum = odd_all_sum + num_16 + num_14 + num_12 + num_10 + num_8 + num_6 + num_4 + num_2;
    
    //variable which takes first 2 numbers:
    int double_number_card = (card / 100000000000000);
    
    //variable which make validation of card:
    int check_card = all_sum % 10;
    
    //add odd numbers for AMEX:
    int odd_all_sum_amex = odd_sum_15 + odd_sum_13 + odd_sum_11 + odd_sum_9 + odd_sum_7 + odd_sum_5 + odd_sum_3;
    
    //add all numbers for AMEX:
    int all_sum_amex = odd_all_sum + num_16 + num_14 + num_12 + num_10 + num_8 + num_6 + num_4 + num_2;
    int double_number_card_amex = (card / 10000000000000);
    
    
    
    //Condition for VISA, MASTERCARD, AMEX - American Express , and INVALID statement: 
    if ((double_number_card_amex == 34 || double_number_card_amex == 37) && (check_card == 0))
    {
        printf("AMEX\n");
    }
    else if ((double_number_card == 51 || double_number_card == 52 || double_number_card == 53 || double_number_card == 54 
              || double_number_card == 55) && (check_card == 0))
    {
        printf("MASTERCARD\n");
    }
    else if ((num_1 == 4) && (check_card == 0))
    {
        printf("VISA\n");
    }
    else 
    {
        printf("INVALID\n");
    }
    
    return 0;
}




