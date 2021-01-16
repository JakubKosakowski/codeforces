#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
	int t, ans=0;
	vector<int> v;
	cin >> t;
	while(t--){
		int a;
		cin>>a;
		v.push_back(a);		
	}
	sort(v.begin(),v.end());
	for(int i = 0; i < v.size(); i+=2){
		ans += v[i+1] - v[i];	
	}
	cout<<ans<<endl;
	return 0;
}
