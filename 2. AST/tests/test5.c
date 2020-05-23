#include<stdio.h>
#include<stdlib.h>


struct person {
	int id;
	int age;
	int can_vote;
};



struct person yash;
struct person sood;
int main()
{

	sood.id = 23;
	sood.age = 312;
	
	yash.id = 213;
	yash.age = 12;
	
	sood.can_vote = sood.age >= 18 ? 1 : 0;
	yash.can_vote = yash.age >= 18 ? 1 : 0;
	
	
}
