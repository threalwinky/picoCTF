#include <bits/stdc++.h>
using namespace std;
#define int long long
#define fi first
#define se second
const int N = 1e6 + 9;
const int N2 = N * 10;
const int mod = 1e9 + 7;
const int inf = LLONG_MAX;



signed main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    if (fopen("TASK.INP", "r")){
    freopen("TASK.INP", "r", stdin);
    freopen("TASK.OUT", "w", stdout);}
    
    string s = "jU5t_a_sna_3lpm18g947_u_4_m9r54f";

    int a[50];
    for (int i=0; i<50; i++){
        a[i] = -1;
    }
    for (int i=0; i<46; i++){
        cout << a[i];
    }
    int i;
    for (i=0; i<8; i++) {
            a[i] = i;
        }
        for (; i<16; i++) {
            a[i] = 23-i;
        }
        for (; i<32; i+=2) {
            a[i] = 46-i;
        }
        for (i=31; i>=17; i-=2) {
            a[i] = i;
        }
    cout << "\n";
    char aa[60];
    for (int i=0; i<46; i++){
        cout << a[i] << " " << s[i] << "\n";
        aa[a[i]] = s[i];
    }
    for (int i=0; i<32; i++){
        cout << aa[i];
    }
}