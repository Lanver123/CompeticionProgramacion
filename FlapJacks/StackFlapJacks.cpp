#include <sstream> //istream
#include <iostream> //cout
#include <math.h>
using namespace std;

void print_array(int *array_ptr, int sub_array_size)
{
	for(int i = 0; i < sub_array_size; i++)
	{	
		cout << array_ptr[i];
		if(i != sub_array_size-1) cout << " ";
	}
	cout << "\n";
}

//Find max value between [start, end]
int find_max_pos(int *array_ptr, int start, int end)
{
	int maxval = -1; int maxpos = -1;
	for(int i = start; i <= end; i++)
	{
		if(array_ptr[i]>maxval)
		{
			maxval = array_ptr[i];
			maxpos = i;
		}
	}
	return maxpos;
}

void flip_array(int *array_ptr, int start, int end)
{
	int middle = ceil((end-start)/2.0 ) + start - 1;
	for(int i = 0; i <= middle-start; i++)
	{
		int aux = array_ptr[i+start];
		array_ptr[i+start] = array_ptr[end-i];
		array_ptr[end-i] = aux;
	}
}

// 0 -> bottom [Max number here]
// array_size - 1 -> top [Min number here]
void sort_spatula(int *array_ptr, int array_size)
{
	int ord = 0;
	while(ord < array_size - 1)
	{
		int max_pos = find_max_pos(array_ptr, ord, array_size-1);
		//Maxpos at bottom
		if(max_pos == ord) {} //Do nothing
		//Maxpos at top
		else if(max_pos == array_size-1)
		{
			flip_array(array_ptr, ord, array_size-1);
			printf("%d ", ord+1);
		}
		//Maxpos in the middle
		else
		{
			//Put maxpos at top
			flip_array(array_ptr, max_pos, array_size-1);
			//Now move from top to bottom
			flip_array(array_ptr, ord, array_size-1);
			printf("%d %d ", max_pos+1, ord+1);
		}

		ord++;
	}
	printf("0\n");	
}

int main(int argc, char * argv[])
{
    int inputArray[5];

    char str[200];

    while(fgets(str, 200, stdin) != NULL)
    {
        istringstream ss(str);
        int num;
		int array_size = 0;
		int problem_array[30];
        while(ss >> num)
		{
			problem_array[array_size] = num;
			array_size++;
		}
		print_array(problem_array, array_size);
		flip_array(problem_array, 0, array_size-1);
		sort_spatula(problem_array, array_size);
    }
    return 0;
}
