#include<iostream>
#include<fstream>
#include<vector>
using namespace std;

int main(int argc, char const *argv[])
{
    ifstream file("d2.txt");
    int depth = 0;
    int horizontal = 0;
    int aim = 0;


    if(file.is_open()) {
        string line;
        string direction;
        int X;
        while(getline(file, line)) {
            int s = line.find(" ");
            direction = line.substr(0, s);
            X = stoi(line.substr(s, line.size()));
            if(direction == "forward") {
                horizontal = horizontal + X;
                depth = depth + (X * aim);
            } else if (direction == "down")
            {
                aim = aim + X;
            } else {
                aim = aim - X;
            }
            
        }
    }

    cout << depth * horizontal << endl;
    return 0;
}