#include <iostream>

using namespace std;

int main(){
	int n, a, b, ans = 0;
	
	cin >> n >> a >> b;
	
	if(a + b < n){
		cout<< b + 1 << endl;
	}
	else{
		while(a != n){
			++ans;
			++a;
			--b;
		}
	
		cout<<ans<<endl;
	}
	
	return 0;
}
