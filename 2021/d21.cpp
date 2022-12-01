#include<iostream>
#include<fstream>
#include<vector>
using namespace std;

int main(int argc, char const *argv[])
{
    ifstream file("d2.txt");
    int depth = 0;
    int horizontal = 0;


    if(file.is_open()) {
        string line;
        string direction;
        int num;
        while(getline(file, line)) {
            int s = line.find(" ");
            direction = line.substr(0, s);
            num = stoi(line.substr(s, line.size()));
            if(direction == "forward") {
                horizontal = horizontal + num;
            } else if (direction == "down")
            {
                depth = depth + num;
            } else {
                depth = depth - num;
            }
            
        }
    }

    cout << depth * horizontal << endl;
    return 0;
}