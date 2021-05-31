#include <iostream>

using namespace std;

int main(){
	int n, m;
	int a = 0;
	cin >> n >> m;
	
	for(int i = 1; i <= n; ++i){
		if(i % 2 == 1){
			for(int j = 1; j <= m; ++j){
				cout<<"#";
			}
			cout<<endl;
		}
		else{
			if(a % 2 == 0){
				for(int k = 1; k <= m; ++k){
					if(k == m){
						cout<<"#";
					}
					else{
						cout<<".";
					}
				}
				cout<<endl;
				++a;
			}
			else{
				for(int k = 1; k <= m; ++k){
					if(k == 1){
						cout<<"#";
					}
					else{
						cout<<".";
					}
				}
				cout<<endl;
				++a;	
			}	
		}
	}
	
	return 0;	
}
