#include <iostream>
#include <vector>

using namespace std;

int main(){
	int t;
	vector<int> v;
	cin >> t;
	for(int i = 0; i < t; ++i){
		long long n, k, ans = 0;
		cin >> n >> k;
		while(n){
			if(n % k){
				ans += n%k;
				n = n/k*k;
			}
			else{
				n /= k;
				++ans;
			}
		}
		cout<<ans<<endl; 
	}
	return 0;
}
