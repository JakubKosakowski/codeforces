#include <iostream>
#include <cstdlib>

using namespace std;

int main(){
	int n;
	cin >> n;
	int g=0,h=0;
	while(n--){
		long x;
		cin >> x;
		if(x%2 == 1){
				++g;	
			}
			else{
				++h;	
			}
	}
	cout<<min(g,h)<<endl;
	return 0;	
}
