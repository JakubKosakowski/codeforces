#include <iostream>
using namespace std;

int main(){
	int t;
	cin >> t;
	while(t--){
		int n;
		cin >> n;
		if(n >= 2 && n <= 7){
			cout<<1<<endl;
		}
		else{
			int g = 2;
			while(true){
				if(n <= g*7){
					cout<<g<<endl;
					break;
				}
				else{
					++g;
				}
			}
		}
	}
	return 0;
}
