#include <iostream>

using namespace std;

int main(){
	int n,b,d;
	cin >> n >> b >> d;
	int ans=0, w=0;
	while(n--){
		int a;
		cin >> a;
		if(a <= b){
			w+=a;
			if(w > d){
				++ans;
				w = 0;
			}
		}
	}
	cout<<ans<<endl;
	return 0;	
}
