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

void writeToFile(string fileName, string content, int offset) {
    fstream f;
    f.open("/Users/bhavdeep/Documents/100DaysOfCode/TextFileHash/" + fileName, ios::out);
    f.seekg(offset);
    string checker;
    content += '%';
    if(f) {
        cout<<"Checker:";
        f.seekg(offset);
        while(checker.length() != content.length()) {
            char c = f.get();
            cout<<checker[checker.length()];
            checker += c;
        }
        cout<<endl;
        bool blank = true;
        for(char c : checker) {
            if(c != char(NULL)) {
                blank = false;
                break;
            }

        }
        cout<<"Blank: "<<blank<<endl;
        if(checker[0] == EOF || !blank)
        {
            //f.seekp(offset);
            f<<content;
        }
        else {
            //TODO: Recursive linear probing?
            return;
        }
    }
    //f<<content;
    f.close();
}


int main() {
    writeToFile("TextFileHashMemory.txt", "hello", 3);
    //cout<<readFromFile("TextFIleHashMemory.txt", 3)<<endl;
    writeToFile("TextFileHashMemory.txt", "he", 0);
    //cout<<readFromFile("TextFileHashMemory.txt", 0)<<endl;
    readAll("TextFileHashMemory.txt");
}