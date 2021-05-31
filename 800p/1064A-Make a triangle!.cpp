#include <iostream>
#include <algorithm>

using namespace std;

int main(){
	int a,b,c;
	
	cin >> a >> b >> c;
	
	int d = max(a,b);
	int e = max(b,c);
	int f = max(d,e);
	
	if(a == b && b == c){
		cout<<0<<endl;
	}
	else{
		if(a == f){
			int ans = b+c;
			if(ans > f){
				cout<<0<<endl;
			}
			else{
				cout<<f-ans+1<<endl;
			}
		}
		else if(b == f){
			int ans = a+c;
			if(ans > f){
				cout<<0<<endl;
			}
			else{
				cout<<f-ans+1<<endl;
			}
		}
		else{
			int ans = a+b;
			if(ans > f){
				cout<<0<<endl;
			}
			else{
				cout<<f-ans+1<<endl;
			}
		}
	}
	
	return 0;	
}
