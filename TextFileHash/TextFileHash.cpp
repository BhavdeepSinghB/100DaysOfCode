#include <iostream>
#include<fstream>
#include<string>
#include<cctype>
using namespace std;

void linearProbing() {
    return;
}

string readFromFile(string fileName, int offset) {
    fstream f;
    string returnable = "";
    f.open("/Users/Bhavdeep/Documents/100DaysOfCode/TextFileHash/" + fileName, ios::in);
    f.seekg(offset);
    if(f) {
        f.seekg(offset);
        char c = f.get();
        returnable += c;
        while (c != '%' && !f.eof()) {
            c = f.get();
            if(c == EOF) {
                continue;
            }
            returnable += c;
        }
        f.close();
        return returnable;
    }
    return "NULL";
}

void writeToFile(string fileName, string content, int offset) {
    fstream f;
    f.open("/Users/bhavdeep/Documents/100DaysOfCode/TextFileHash/" + fileName, ios::out | ios::in);
    f.seekg(offset);

    if(f) {
        string fileContent = readFromFile(fileName, offset);
        if(fileContent.empty() || fileContent[0] == EOF) {
            //TODO: Figure out a way to read the content size with minimum code
            //Comment - Might have to change the entire blueprint of the program
        }

    }
}


int main() {
    writeToFile("TextFileHashMemory.txt", "hello", 3);
    cout<<readFromFile("TextFIleHashMemory.txt", 3);
}