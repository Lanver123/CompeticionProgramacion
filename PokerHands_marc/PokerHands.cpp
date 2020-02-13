/*
    C, D, H, S
    2,3,4,5,6,7,8,9,T(10),J(11),Q(12),K(13),A(14)
*/

//SE DEVUELVE UN ARRAY DE INTS CON LOS VALORES 
//EN ORDEN DE PRIORIDAD PARA EL DESEMPATE

#include <stdlib.h>     /* atoi */
#include <cstdio>
//Return 1 if card1 >= card2. Else 0
int compare_cards(char card1, char card2)
{
    if(card1 == 'A') return 1;
    if(card1 == 'K' && card2 != 'A') return 1;
    if(card1 == 'Q' && card2 != 'A' && card2 != 'K') return 1;
    if(card1 == 'T' && card2 != 'A' && card2 != 'K' && card2 != 'Q') return 1;
    //A partir de aqui card1 esta en [2,9]
    //Si card2 es [A,K,Q,T]
    if(card2 >= 65) return 0;

    //A partir de aqui ambas son numeros
    return card1 >= card2;
}

void swap(const char **hand, int pos1, int pos2)
{
    const char *aux = hand[pos1];
    ///
    hand[pos1] = hand[pos2];
    hand[pos2] = aux;
}

int partition(const char **hand, int low, int high)
{
    // pivot (Element to be placed at right position)
    const char *pivot = hand[high];  
 
    int i = (low - 1) ; // Index of smaller element

    for (int j = low; j < high; j++)
    {
        // If current element is smaller than the pivot
        // (If current element is not bigger or equal than the pivot)
        if(!compare_cards(hand[j][0], pivot[0]))
        {
            i++;    // increment index of smaller element
            swap(hand, i, j);        
        }
    }
    swap(hand, i+1, high);
    return (i + 1);
}

void quickSort(const char **hand, int low, int high)
{
    if (low < high)
    {
        int pi = partition(hand, low, high);
        quickSort(hand, low, pi - 1); 
        quickSort(hand, pi + 1, high);
    }
}

int *hand_value(const char **hand)
{
    int res[5];
    /*  Escalera color [5000+14]        MAX_VAL = 5014
        4 iguales [3000+14,13]          MAX_VAL = 3014
        3+2      [1000+100*14+13]       MAX_VAL = 2413
        5 color  [700+14]               MAX_VAL = 714
        Escalera [600+14]               MAX_VAL = 614
        3   [500+14, 4,3]               MAX_VAL = 514
        2+2 [200+2*14 + 200+2*13, 9]    MAX_VAL = 454
        2: [100+2, 5, 3, 2]             MAX_VAL = 114
        High Card: [14, 9, 6, 4, 2]     MAX_VAL = 14
    */

    //Es una escalera?
    int escalera = 0;
    //if(hand[i][1] + 1)
    
    return res;
}

int main(int argc, char const *argv[])
{
    const char **hand1 = (const char**) malloc(sizeof(char*)*5);
    hand1[0] = "AH";
    hand1[1] = "KD";
    hand1[2] = "QS";
    hand1[3] = "TC";
    hand1[4] = "9D";

    const char **hand2 = (const char**) malloc(sizeof(char*)*5);
    hand2[0] = "2C";
    hand2[1] = "3H";
    hand2[2] = "4S";
    hand2[3] = "8C";
    hand2[4] = "AH";

    quickSort(hand1, 0, 4);
    return 0;
}
