/*
Author : Dhruv B Kakadiya

*/

#include <stdio.h>
#include <string.h>
int main()
{
    int num, i = 0;
    char c, checksum, buff[9];
    FILE *fp = fopen("sender_file.txt", "r");
    FILE *fp2 = fopen("recieved_file.txt", "w");
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
    while (1)
    {
        c = fgetc(fp);
        buff[i] = c;
        if (c == EOF)
        {
            break;
        }
        i++;
        if (i == 9)
        {
            char temp = buff[0];
            fputc(buff[0], fp2);
            for (int j = 1; j < 8; j++)
            {
                fputc(buff[j], fp2);
                temp = temp ^ buff[j];
            }
            checksum = temp;
            if (checksum != buff[8])
            {
                printf("Error in content!!!");
                return (1);
            }
            i = 0;
        }
    }
    if (i != 0)
    {
        char temp = buff[0];
        fputc(buff[0], fp2);
        for (int j = 1; j < i - 1; j++)
        {
            fputc(buff[j], fp2);
            temp = temp ^ buff[j];
        }
        checksum = temp;
        if (checksum != buff[i - 1])
        {
            return (1);
        }
    }
    fclose(fp);
    fclose(fp2);
    getch();
    return 0;
}