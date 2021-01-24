#include <iostream>
#include <vector>

using namespace std;

int main(){
	int t;
	vector<long long> v;
	cin >> t;
	while(t--){
		long long a;
		cin >> a;
		v.push_back(a);
	}
	int d = 1, max = 1;
	for(int i = 0; i < v.size()-1; ++i){
		if(v[i] <= v[i+1]){
			++d;
			if(d > max){
				max = d;
			}
		}
		else{
			d = 1;
		}	
	}
	cout<<max<<endl;
	return 0;
}
