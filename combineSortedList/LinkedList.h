//
// Created by Bhavdeep Singh on 2019-04-24.
// Time complexity - O(n)
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

        bool isEmpty() {
            if(head == nullptr)
                return true;
            return false;
        }

        LinkedList combineList(LinkedList l2) {
            LinkedList combinedList;
            Node* p = this->head;
            Node* q = l2.head;

            while(p!=nullptr || q!=nullptr) {
                if(p == nullptr && q != nullptr) {
                    combinedList.append(q->getVal());
                    q = q->getNext();
                }
                else if(q == nullptr && p != nullptr) {
                    combinedList.append(p->getVal());
                    p = p->getNext();
                }
                else {
                    if(p -> getVal() < q->getVal()) {
                        combinedList.append(p->getVal());
                        p = p->getNext();
                    }
                    else {
                        combinedList.append(q->getVal());
                        q = q->getNext();
                    }
                }
            }

            return combinedList;
        }
};
#endif //UNTITLED1_LINKEDLIST_H
