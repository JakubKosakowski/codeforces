#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
	int n,m;
	vector<int> v;
	cin >> n >> m;
	for(int i = 0; i < n; ++i){
		int a;
		cin >> a;
		v.push_back(a);
	}
	sort(v.begin(), v.end());
	int g = n-1, p = 0, ans = 0;
	while(true){
		if(ans < m){
			ans += v[g];
			--g;
			++p;
		}	
		else{
			cout<<p<<endl;
			break;
		}
	}
	return 0;
}
