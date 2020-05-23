#include<stdio.h>
#include<string.h>
struct op
{
    char l;
    char r[20];
}

op[10], pr[10];
int main()
{
    int a, i, k, j, n, z = 0, m, q;
    char * p, * l;
    char temp, t;
    char * tem;
    scanf("%d", &n);
    for (i = 0; i <n; i++)
    {
        getchar();
        op[i].l = getchar();
        scanf(" = %s", op[i].r);
    }
    printf("Intermediate Code:\n");
    for (i = 0; i <n; i++)
    {
        printf("%c = ", op[i].l);
        printf("%s\n", op[i].r);
    }
    //Dead Code Elimination
    for (i = 0; i <n - 1; i++)
    {
        temp = op[i].l;
        for (j = 0; j <n; j++)
        {
            p = strchr(op[j].r, temp);
            if (p)
            {
                pr[z].l = op[i].l;
                strcpy(pr[z].r, op[i].r);
                z++;
            }
        }
    }
    pr[z].l = op[n - 1].l;
    strcpy(pr[z].r, op[n - 1].r);
    z++;
    //Removing common expressions
    for (m = 0; m <z; m++)
    {
        tem = pr[m].r;
        for (j = m + 1; j <z; j++)
        {
            p = strstr(tem, pr[j].r);
            if (p)
            {
                t = pr[j].l;
                pr[j].l = pr[m].l;
                for (i = 0; i <z; i++)
                {
                    l = strchr(pr[i].r, t);
                    if (l)
                    {
                        a = l - pr[i].r;
                        pr[i].r[a] = pr[m].l;
                    }
                }
            }
        }
    }
    printf("\nOptimized Intermediate Code: (removed dead code and common expressions)\n");
    temp='\0';
    char temp2[20]="";
    for (i = 0; i < z; i++)
        if (pr[i].l != '\0')
        {
            if(temp==pr[i].l && strcmp(temp2,pr[i].r)==0)
                continue;
            printf("%c = %s\n", pr[i].l, pr[i].r);
            temp = pr[i].l;
            strcpy(temp2, pr[i].r);
        }
    return 0;
}
