#include <iostream>

using namespace std;
string s[60];
int main(void){
  int N;
  cin >> N;
  int i;
  for (int i=0;i<N;i++) cin >> s[i];
  string ans;
  for(char c="a";c<="z";c++){
    int small = 60;
    for (int i=0;i<N;i++){
      int cnt = 0;
      for(int j=0;j<s[i].length();j++)//cが何回現れるか
	if(s[i][j]==c) cnt++;
      small = min(small,cnt);
    }
    for(int i=0;i<small;i++) ans+=c;
  }
  cout << ans <<endl;
  return 0;
}
