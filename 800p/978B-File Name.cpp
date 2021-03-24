#include <iostream>

using namespace std;

int main(){
	int n, m=0, b=0;
	string s;
	cin >>n;
	cin>>s;
	for(int i = 0; i < n; ++i){
		if(s[i] == 'x'){
			++m;
		}
		else{
			if(m > 2){
				b += (m-2);
				m=0;	
			}
			else{
				m=0;
			}
		}
	}
	if(m > 2){
		b += (m-2);
	}
	cout<<b<<endl;
	return 0;	
}
