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
    return "NO";
}

void readAll(string fileName) {
    fstream f;
    f.open("/Users/bhavdeep/Documents/100DaysOfCode/TextFileHash/" + fileName, ios::in);
    f.seekg(0);
    //string s;
    while(!f.eof()) {
        char c = f.get();
        cout<<c;
    }
}

bool isBlank(string str) {
    for(char c : str) {
        if (c != NULL)
            return false;
        return true;
    }
}

void writeToFIle(string fileName, int offset, string content) {
    fstream f;
    f.open("/Users/bhavdeep/Documents/100DaysOfCode/TextFileHash/" + fileName, ios::in);
    if(f) {
        f.seekg(offset);
        string checker;
        while(checker.length() < content.length()) {
            char c = f.get();
            checker += c;
        }
        if(isBlank(checker) || checker[0] == EOF) {
            f.close();
            f.open("/Users/bhavdeep/Documents/100DaysOfCode/TextFileHash/" + fileName, ios::app);
            f.seekp(offset);
            f<<content;
            f.close();
            return;
        }
        //else
            //TODO: Linear probing
        f.close();
    }
}


int main() {
    fstream f;

    writeToFIle("TextFileHashMemory.txt", 6, "Yos");
    cout<<readFromFile("TextFileHashMemory.txt", 0);
    //readAll("TextFileHashMemory.txt");
}