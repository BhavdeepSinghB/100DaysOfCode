#include <iostream>
#include<fstream>
#include<string>
#include<cctype>
using namespace std;
const string FILENAME = "TextFileHashMemory.txt";

/*void linearProbing() {
    return;
}*/

void init() {
    fstream f;
    f.open("/Users/Bhavdeep/Documents/100DaysOfCode/TextFileHash/" + FILENAME, ios::app | ios::in);
    for(int i = 0; i<10000; i++) {
            f<<" ";
    }
    f.close();

}

int hashfunc(string content) {
    return content.length();
}

string readFromFile(int offset) {
    fstream f;
    string returnable;
    f.open("/Users/Bhavdeep/Documents/100DaysOfCode/TextFileHash/" + FILENAME, ios::in);
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

void readAll() {
    fstream f;
    f.open("/Users/bhavdeep/Documents/100DaysOfCode/TextFileHash/" + FILENAME, ios::in);
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

void writeToFile(string content) {
    fstream f;
    f.open("/Users/bhavdeep/Documents/100DaysOfCode/TextFileHash/" + FILENAME, ios::in);
    if(f) {
        int offset = hashfunc(content);
        bool written = false;
        do {
            f.seekg(offset);
            string checker;
            content += '%';
            while(checker.length() < content.length()) {
                char c = f.get();
                checker += c;
            }
            cout<<checker<<endl;
            if(isBlank(checker) || checker[0] == EOF) {
                f.close();
                f.open("/Users/bhavdeep/Documents/100DaysOfCode/TextFileHash/" + FILENAME, ios::app);
                f.seekp(0, ios::beg);
                f.seekp(offset, ios::end);
                f<<content;
                f.close();
                written = true;
                return;
            }

            f.close();
            content.pop_back();
            offset += content.length();
        } while(!written);

        //cout<<"Occupied, moving "<<content.length()<<" characters"<<endl;
        //writeToFile(fileName, offset+content.length(), content);

    }
}


/*
bool find(string content, int offset) {

}
*/

bool find(string content) {
    fstream f;
    f.open("/Users/bhavdeep/Documents/100DaysOfCode/TextFileHash/" + FILENAME, ios::in);
    string checker = "";
    f.seekg(ios::beg);
    int offset = hashfunc(content);
    if(f) {
        do {
            f.seekg(offset);
            checker = readFromFile(offset);
            cout<<checker<<endl;
            if(checker == content) {
                return true;
            }
            offset += content.length();
        } while(checker.length() == content.length() - 1);
        return false;
    }
    return false;
}




int main() {
    //init();
    //writeToFile("Hello");
    //writeToFile("Yos");
    writeToFile("MaridharEetheUtha");
    readAll();
    //cout<<"\n"<<find("MaridharEetheUtha");

}