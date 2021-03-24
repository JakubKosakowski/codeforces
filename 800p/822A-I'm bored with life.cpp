#include <iostream>

using namespace std;

int main(){
	long a,b;
	long x=1;
	cin>>a>>b;
	if(a > b){
		for(int i = 1; i <= b; ++i){
			x *= i;
		}
		cout<<x<<endl;
	}
	else{
		for(int i = 1; i <= a; ++i){
			x *= i;
		}
		cout<<x<<endl;	
	}
	return 0;	
}
