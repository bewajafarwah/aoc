#include<iostream>
#include<fstream>
#include<vector>
using namespace std;

int main(int argc, char const *argv[])
{

    vector<int> nums;
    int prev = 0;
    int count = 0;
    ifstream file("p1.txt");



    if(file.is_open()) {
        string line;
        int num;
        while(getline(file, line)) {
            num = stoi(line.c_str());
            nums.push_back(num);
        }
    }

    for(int i =  0; i < nums.size(); i++) {
            if(nums[i] > prev) {
                count++;
            }
            prev = nums[i];
    }

    cout << count - 1 << endl;
    return 0;
}