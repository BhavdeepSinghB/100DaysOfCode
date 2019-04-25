//
// Created by Bhavdeep Singh on 2019-04-24.
//

#ifndef UNTITLED1_NODE_H
#define UNTITLED1_NODE_H


class Node {
    private:
        int value;
        Node* next;
    public:
        void setValue(int val) {
            this->value = val;
        }
        void setNext(Node* nex) {
            this->next = nex;
        }
        int getVal() {
            return this->value;
        }
        Node* getNext() {
            return this->next;
        }
};


#endif //UNTITLED1_NODE_H
