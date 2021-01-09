#include <iostream>
#include <string>
using namespace std;

int main(){
	int t;
	cin >> t;
	while(t--){
		int n, p = 0;
		string s;
		cin >> n >> s;
		int g = n-1;
		while(true){
			if(s[g] == ')'){
				++p;
				--g;
			}
			else{
				break;
			}	
		}
		int d = n-p;
		if(p <= d){
			cout<<"No"<<endl;
		}
		else{
			cout<<"Yes"<<endl;
		}
	}
	return 0;
}
