#include<iostream>
#include<fstream>
#include<vector>
#include<algorithm>
#include<cmath>
using namespace std;

int str2dec(string value) {
    int dec = 0;
    int b;
    int j = 0;
    for(int i = value.size() - 1; i >= 0 ; i--) {
        b = (int)value[i] - 48;
        dec = dec + (b * pow(2, j));
        j++;
        
    }
    return dec;
}

int main(int argc, char const *argv[])
{
    ifstream file("d3.txt");
    vector<string> bin;


    if(file.is_open()) {
        string line;
        while(getline(file, line)) {
            bin.push_back(line);
        }
    }

    string eps = "";
    string gamma = "";
    int binary_size = bin[0].size();
    for(int i = 0; i < binary_size; i++) {
        int c0 = 0;
        int c1 = 0;
        for(int j = 0; j < bin.size(); j++) {
            if(bin[j][i] == '0') {
                c0++;
            } else  {
                c1++;
            }
            //cout << c0 <<  " " << c1 << endl;
        }
        if(c1 > c0) {
            gamma.append("1");
            eps.append("0");
        } else {
            gamma.append("0");
            eps.append("1"); 
        }
    }

    cout << eps << " " << gamma << endl;
    cout << str2dec(eps) << " " << str2dec(gamma) << endl;
     cout << str2dec(eps) * str2dec(gamma) << endl;
    return 0;
}