/* PROBLEM STATEMENT
    10 REGISTERS: INITIALLY 000
    1000 WORDS OF RAM: VALUES IN RANGE[000,999]
    FIRST INSTRUCTION AT ADDRESS 0
    ALL RESULTS %1000

    INPUT:
        #CASES

    {   RAM[0]
  CASE  RAM[1]
        ...
    }   RAM[999] // SI LLEGA

    OUTPUT:
        #INSTRUCCIONES EJECUTADAS HASTA
        HALT (INCLUSIVE)
*/

#include <sstream> //istream
#include <iostream> //cout
#include <string> 
#include <math.h>
#include <assert.h>     /* assert */
using namespace std; 

int ram[1000];
int registers[10];
int inst_ptr;
int halted;

void initalize_memory()
{
    halted = 0;
    inst_ptr = 0;
    for(int i = 0; i < 10; i++) registers[i] = 0;
    for(int i = 0; i < 1000; i++) ram[i] = 0; 
}

void operation(int opcode)
{
    int opnum = opcode / 100;
    int op1 = (opcode%100)/10;
    int op2 = opcode%10;
    switch(opnum)
    {
        case 1: 
            halted = 1;
            break;
        case 2:
            registers[op1] = op2;

            break;
        case 3:
            registers[op1] = (registers[op1] + op2)%1000;
            break;
        case 4:
            registers[op1] = (registers[op1] * op2)%1000;
            break;
        case 5: 
            registers[op1] = registers[op2];
            break;
        case 6: 
            registers[op1] = (registers[op1] + registers[op2])%1000;
            break;
        case 7: 
            registers[op1] = (registers[op1] * registers[op2])%1000;
            break;
        case 8: 
            registers[op1] = ram[registers[op2]];
            break;
        case 9:
            ram[ registers[op2] ] = registers[op1];
            break;
        case 0: 
            if(registers[op2] != 0)
            {
                inst_ptr = registers[op1];
                goto end_op;
            }
            break;
    }
    inst_ptr++;
    end_op: return;
}

int run_program()
{
    int num_instrs = 0;
    while(!halted)
    {
        operation(ram[inst_ptr]);
        num_instrs++;
    }

    printf("%d\n", num_instrs);
    return num_instrs;
}

int main(int argc, char * argv[])
{
    int num_cases;
    string line;
    
    getline(cin, line);
    istringstream iss (line);
    iss >> num_cases;
    getline(cin, line);
    for(int caso = 1; caso <= num_cases; caso++)
    {
        initalize_memory();
        int i = 0;
        while (getline(cin, line))        
        {
            assert(i < 1000);
            if(line == "") goto end_loop;
            int num = stoi(line);
            ram[i] = num;
            i++;
        }
    end_loop: run_program();
        if(caso < num_cases) cout << endl;
    }
    return 0;
}