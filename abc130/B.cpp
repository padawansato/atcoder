#include <iostream>
using namespace std;

int main(){
    int n,x;
    cin >> n >> x;
    vector<int> l(n)
    for (int i=0;i < n;i++)
        cin >> l[i]
    }
    int ans = 1;
    int p = 0;
    for (int i=0;i < x;i++){
        p += l[i]
        if (p <= x) ans++;
    }
    cout << ans << endl;
    return 0
}
