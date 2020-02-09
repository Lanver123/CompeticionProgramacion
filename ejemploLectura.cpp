#include <sstream> //istream
#include <iostream> //cout
#include <fstream> //ifstream

using namespace std;

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

