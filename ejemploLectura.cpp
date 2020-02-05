#include <sstream> //istream
#include <iostream> //cout
#include <fstream> //ifstream

using namespace std;

void flip_sub_array(int *array_ptr, int array_size, int flip_point)
{
    //Array empieza en 0 pero flip_point 1 es el de 0
    for(int i = flip_point-1; i < array_size; i++)
}
int main(int argc, char * argv[])
{
    std::ifstream myfile("example.txt");

    int inputArray[5];

    string str;

    while(getline(myfile, str))
    {
        istringstream ss(str);
        int num;
        while(ss >> num)
        {
            cout << num << " ";
        }
    }

    myfile.close();
    return 0;
}

