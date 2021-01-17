#include <iostream>

using namespace std;

int main(){
	int a1,a2,a3,b1,b2,b3,n;
	cin>>a1>>a2>>a3;
	cin>>b1>>b2>>b3;
	cin>>n;
	int swc = 0, swm = 0, ac = a1+a2+a3, am = b1+b2+b3;
	while(ac > 0){
		++swc;
		ac -= 5;
	}	
	while(am > 0){
		++swm;
		am -= 10;
	}
	if(swc+swm <= n){
		cout<<"YES"<<endl;
	}
	else{
		cout<<"NO"<<endl;
	}	
	return 0;
}
