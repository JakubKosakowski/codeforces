#include <iostream>
#include <cstdlib>

using namespace std;

int main(){
	int t;
	cin >> t;
	while(t--){
		int n,k;
		cin >> n >> k;
		
		if(n == k){
			cout<<0<<endl;
		}	
		else if (n < k){
			cout<<abs(n-k)<<endl;
		}
		else{
			if((n-k) % 2 == 1){
				cout<<1<<endl;
			}
			else{
				cout<<0<<endl;
			}
		}
	}
	return 0;	
}
