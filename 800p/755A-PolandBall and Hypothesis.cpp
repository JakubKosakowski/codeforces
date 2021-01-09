#include <iostream>
using namespace std;

int main(){
	int n, m = 1;
	cin >> n;
	while(true){
		int p = n*m+1, d = 0;
		for(int i = 2; i < p; ++i){
			if(p % i == 0){
				++d;
			}
		}
		if(d != 0){
			cout<<m<<endl;
			break;
		}
		else{
			++m;
		}	
	}
	return 0;
}
