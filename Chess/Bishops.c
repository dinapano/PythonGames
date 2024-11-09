#include <stdio.h>

int main(void)
{
	int i,j,X,Y;
	int N=8;
	int skakiera[8][8]={0};
	
	printf("Dwse thn thesh tou Aksiwmatikou (X,Y): \n");
	scanf("%d", &X);
	scanf("%d", &Y);
	
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
	printf("\nSkakiera me enan Aksiwmatiko: \n");
	
	for(i=0;i<N;i++)
	{
		for(j=0;j<N;j++)
		{
			if(i==j)
			{
				skakiera[i][j]=1;
			}
			else
			{
				skakiera[i][j]=0;
			}
		}
	}
	
	for(i=0;i<N;i++)
	{
		for(j=0;j<N;j++)
		{
			if(i==X && j==Y)
			{
				printf("A");
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

