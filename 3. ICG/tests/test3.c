#include <stdio.h>
int main()
{
	int a=5;
	int b=6;
    if(b<9)
    {
        a=2;
    }
    else
    {
        a=4;
    }
	while(a<20)
	{
		b=b+1;
		a=a+1;
	}
	return 0;
}
