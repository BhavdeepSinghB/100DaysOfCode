//
// Created by Bhavdeep Singh on 2019-04-24.
//
#include<iostream>
#include "Node.h"
#ifndef UNTITLED1_LINKEDLIST_H
#define UNTITLED1_LINKEDLIST_H

using namespace std;

class LinkedList {
    private:
        Node* head;
    public:
        LinkedList() {
            head = nullptr;
        }

        void append(int number) {
            if(head == nullptr) {
                head = new Node();
                head->setValue(number);
                head->setNext(nullptr);
                return;
            }
            Node* p = head;
            while(p->getNext() != nullptr) {
                p = p->getNext();
            }
            p->setNext(new Node());
            p = p->getNext();
            p->setNext(nullptr);
            p->setValue(number);
        }

        void print() {
            Node* p = head;
            while(p != nullptr) {
                cout<<p->getVal()<<" ";
                p = p->getNext();
            }
        }
};
#endif //UNTITLED1_LINKEDLIST_H
