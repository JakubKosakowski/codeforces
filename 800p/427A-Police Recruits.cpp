#include <iostream>
using namespace std;

int main(){
	int t, ans = 0, o =0;
	cin >> t;
	while(t--){
		int n;
		cin >> n;
		if(n < 0){
			if(o == 0){
				++ans;
			}
			else{
				--o;
			}
		}
		else{
			o += n;
		}	
	}
	cout<<ans<<endl;
	return 0;
}
