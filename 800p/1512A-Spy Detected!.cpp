#include <iostream>

using namespace std;

int main(){
	int t;
	cin >> t;
	while(t--){
		int n;
		cin >> n;
		int *p = new int[n];
		for(int i = 0; i < n; ++i){
			int a;
			cin >> a;
			p[i] = a;
		}
		for(int i = 0; i < n-1; ++i){
			if(i == 0){
				if(p[i] != p[i+1]){
					if(p[i] == p[i+2]){
						cout<<i+2<<endl;
						break;
					}	
					else if(p[i+1] == p[i+2]){
						cout<<i+1<<endl;
						break;
					}
				}	
			}
			else{
				if(p[i] != p[i+1]){
					cout<<i+2<<endl;
					break;
				}
			}
		}
	}
	return 0;	
}
