#include <iostream>

using namespace std;

int main(){
	int t;
	cin >> t;
	while(t--){
		long n,k;
		cin >> n >> k;
		int s=0;
		for(int i = 2; i <= n/2; ++i){
			if(n%i==0){
				cout<<n+i+2*(k-1)<<endl;
				++s;
				break;
			}
		}
		if(s == 0){
			cout<<2*n+2*(k-1)<<endl;
		}
	}
	return 0;	
}
