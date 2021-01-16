#include <iostream>

using namespace std;

int main(){
	int t;
	cin >> t;
	while(t--){
		int n,m, ans=0;
		cin>>n>>m;
		for(int i = 0; i < n; ++i){
			int a;
			cin >> a;
			ans += a;
		} 	
		if(ans == m){
			cout<<"YES"<<endl;
		}
		else{
			cout<<"NO"<<endl;
		}
	}
	return 0;
}
