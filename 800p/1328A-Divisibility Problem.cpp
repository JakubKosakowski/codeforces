#include <iostream>

using namespace std;

int main(){
	int t;
	
	cin >> t;
	
	while(t--){
		long a,b;
		
		cin >> a >> b;
		
		if(a < b){
			cout<<b-a<<endl;
		}
		else{
			if(a % b == 0){
				cout<<0<<endl;
			}
			else{
				cout<<b-(a%b)<<endl;
			}
		}
	}
	
	return 0;	
}
