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
    string returnable;
    f.open("/Users/Bhavdeep/Documents/100DaysOfCode/TextFileHash/" + fileName, ios::in);
    f.seekg(offset);
    if(f) {
        f.seekg(offset);
        char c = f.get();
        returnable += c;
        while (!f.eof()) {
            c = f.get();
            if(c == EOF) {
                continue;
            }
            if(c == '%') {
                return returnable;
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
    string checker;
    content += '%';
    if(f) {
        f.seekg(offset);
        while(checker.length() != content.length()) {
            char c = f.get();
            //cout<<checker[checker.length()];
            checker += c;
        }
        bool blank = true;
        for(char c : checker) {
            if(!isblank(c))
                blank = false;
        }
        if(checker[0] == EOF || !blank)
        {
            f.seekp(offset);
            f<<content;
        }
        else {
            //TODO: Recursive linear probing?
            return;
        }
    }
}


int main() {
    writeToFile("TextFileHashMemory.txt", "hello", 3);
    cout<<readFromFile("TextFIleHashMemory.txt", 3)<<endl;
    writeToFile("TextFileHashMemory.txt", "he", 0);
    cout<<readFromFile("TextFileHashMemory.txt", 0)<<endl;
}