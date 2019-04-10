#include <iostream>
#include<fstream>
#include<string>
#include<cctype>
using namespace std;

string readFromFile(string fileName, int offset) {
    fstream f;
    string returnable;
    f.open("/Users/bhavdeep/Documents/100DaysOfCode/TextFileHash/" + fileName, ios::in);
    if(f) {
    f.seekg(offset);
        while (!f.eof()) {
            char c = f.get();
            if(c == EOF) {
                continue;
            }
            cout<<c;
        }
        f.close();
        return "something";
    }
    return "something else";
}

void writeToFile(string fileName, string content, int offset) {
    fstream f;
    f.open("/Users/bhavdeep/Documents/100DaysOfCode/TextFileHash/" + fileName, ios::out);
    f<<"Hello";
}

int main() {
    //writeToFile("textMemory.txt", "hello", 3);
    readFromFile("main.cpp", 0);
}