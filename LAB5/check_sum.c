/*
Author : Dhruv B Kakadiya

*/

#include<stdio.h>
#include<string.h>
int main()
{
    int num, i = 0;
    char c, checksum, buff[8];
    FILE* fp = fopen("original.txt", "r");
    FILE* fp2= fopen("sender_file.txt","w");
    if (fp == NULL)
    {
        printf("Error while Opening file!\n");
        return (1);
    }
    if (fp2 == NULL)
    {
        printf("Error while Opening file!\n");
        return (1);
    }
    while(1)
    {
        c = fgetc(fp);
        buff[i]= c;
        if (c == EOF)
        {
            break;
        }
        fputc(c, fp2);
        printf("%c", c);
        i++;
        if(i == 8)
        {
            char temp = buff[0];
            for(int j = 1 ; j < i ; j++)
            {
                temp = temp ^ buff[j];
            }
            checksum = temp;
            fputc(checksum, fp2);
            printf("%c", checksum);
            i = 0;
        }
    }
    if(i != 0)
    {
        char temp = buff[0];
        for(int j = 1 ; j < i ; j++)
        {
            temp = temp ^ buff[j];
        }
        checksum = temp;
        fputc(checksum, fp2);
        printf("%c", checksum);
    }
    fclose(fp);
    fclose(fp2);
    getch();
    return (0);
}
