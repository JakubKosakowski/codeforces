#include <iostream>
using namespace std;

int main(){
	int t, x, y;
	cin >>t;
	while(t--){
		cin >>x >>y;
		if(x < y){
			if(x == 1){
				cout<<"No"<<endl;
			}
			else{
				while(x < y && x != 3){
					if(x % 2){
						x--;
					}
					else{
						x /= 2;
						x *= 3;
					}
				}
				if(x >= y){
					cout<<"Yes"<<endl;
				}
				else{
					cout<<"No"<<endl;
				}	
			}	
		}
		else{
			cout<<"Yes"<<endl;		
		}
	}
	return 0;
}
