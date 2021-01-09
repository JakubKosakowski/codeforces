#include <iostream>
using namespace std;

int main(){
	int n, p = 0;
	cin >> n;
	while(n--){
		int a,b;
		string s;
		cin >> s >> a >> b;
		if(b - a > 0 && a >= 2400){
			++p;
		}
	}
	if(p != 0){
		cout<<"YES"<<endl;
	}
	else{
		cout<<"NO"<<endl;
	}
	return 0;
}
