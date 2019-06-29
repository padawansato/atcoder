//passwordが入って時
//E=asod,O=pswr
#include <iostream>
#include <algorithm>
using namespace std;
string O,E;
int main(void){
  cin >> O >> E;
  int N = O.length() + E.length();
  string ans;
  for (int i=0; i<N; i++){//0から
    if(i%2 == 0){
      ans += O[i/2];
    }
    else{
      ans += E[i/2];
    }
  }
  cout << ans << endl;
  return 0;
}
