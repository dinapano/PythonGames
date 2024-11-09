#include <stdio.h>

int main(void)
{
	int i,j,X,Y;
	int N=8;
	int skakiera[8][8]={0};
	
	printf("Dwse thn thesh tou purgou(X,Y), opou 1<=X,Y<=8: \n");
	scanf("%d", &X);
	X=X-1;
    scanf("%d", &Y);
	Y=Y-1;
	
	for(i=0;i<N;i++)
	{
		for(j=0;j<N;j++)
		{
			if(i==X || j==Y)
			{
				skakiera[i][j]=1;
			}
		}
	}
	printf("\nSkakiera me ena purgo: \n");
	
	for(i=0;i<N;i++)
	{
		for(j=0;j<N;j++)
		{
			if(i==X && j==Y)
			{
				printf("P ");
			}
			else
			{
				printf("%d", skakiera[i][j]);
			}
		}
		printf("\n");
	}
	
	return 0;	
}

