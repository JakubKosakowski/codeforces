#include <iostream>
using namespace std;

int main(){
	int n,m, a = 0;
	cin >> n >> m;
	while(n--){
		int x, g = 0;
		cin >> x;
		a += x;
		int d = a/m;
		if(d > 0){
			cout<<d<<endl;
			a -= d*m;
		}
		else{
			cout<<0<<endl;
		}
	}
	return 0;
}
