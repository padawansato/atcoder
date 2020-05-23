#include <bits/stdc++.h>
using namespace std;

int main() {
  vector<int> vec(1) ;
  int s;
  cin >> s;
  for (i = 0; i*2019<s; i++){
  	vec.push_back(i*2019)
  }
  // 3の要素を指すイテレータ
  int i = 0;
  while (i*2019 < s){
  auto itr = find(s.begin(), s.end(), vec[i]);
	i++;
  }
  // もし存在しなければ、a.end()が返る
  if (itr == a.end()) {
    cout << "not found" << endl;
  } else {
    // itrが添字の何番目を指すかを求める
    int idx = distance(a.begin(), itr);
    cout << "a[" << idx << "] = " << *itr << endl;
  }
}

