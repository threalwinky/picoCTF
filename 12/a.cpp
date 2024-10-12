#include<bits/stdc++.h>
using namespace std;
int main(){
    freopen("a", "r", stdin);
    int x;
    char y;
    int a[60];
    while (cin >> x){
        cin >> y;
        a[x] = y;
    }
    for (int i=0; i<32; i++){
        cout << char(a[i]);
    }
}