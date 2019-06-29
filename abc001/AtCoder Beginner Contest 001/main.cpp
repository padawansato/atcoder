//////
//////  main.cpp
//////  AtCoder Beginner Contest 001
//////
//////  Created by Takumi Sato on 2017/03/03.
//////  Copyright © 2017年 Takumi Sato. All rights reserved.
//////
////
////#include <iostream>
////using namespace std;
////int main() {
////    int a;
////    int b;
////    cin >> a;
////    cin >> b;
////    cout << (a-b);
////    cout << endl;
////    return 0;
////}
//
//#include <iostream>
//using namespace std;
//int main(){
//    int m,n;
//    cin >> m;
//    n << (m+50);
//    cout << n/1000;
//    if (m<1000) {
//        cout
//    }
//}
//
#include<vector>
#include<list>
#include<stack>
#include<queue>
#include<algorithm>
using namespace std;


int main(){
    int m;
    scanf("%d",&m);
    if (m<100) {
        printf("00\n");
    } else if (m<=5000) {
        printf("%02d\n",m/100);
    } else if (m>=6000 && m<=30000) {
        printf("%d\n",m/1000+50);
    } else if (m>=35000 && m<=70000) {
        printf("%d\n",(m/1000-30)/5+80);
    } else {
        printf("%d\n",89);
    }
    return 0;
}
