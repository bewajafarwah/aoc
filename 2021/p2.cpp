#include<iostream>
#include<fstream>
#include<vector>
using namespace std;

int main(int argc, char const *argv[])
{

    vector<int> nums;
    int prev = 0;
    int step = 3;
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

    int i = 0;
    int sum = 0;
    while(true) {
        if(i + step > nums.size()) {
            break;
        }

        sum = nums[i] + nums[i + 1] + nums[i + 2];
        if(sum > prev) {
            count++;
        }
        prev = sum;
        i++;
    }

    cout << count - 1 << endl;
    return 0;
}