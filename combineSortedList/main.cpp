#include<iostream>
#include "linkedList.h"
#include "Node.h"
using namespace std;


int main() {
    LinkedList l1, l2, l3;

    l1.append(1);
    l1.append(2);
    l1.append(3);

    l2.append(1);
    l2.append(3);
    l2.append(5);

    l1.print();
    cout<<endl;
    l2.print();
    cout<<endl;
    l3 = l1.combineList(l2);
    l3.print();
}