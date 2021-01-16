#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
	int n, ans = 0, p, d, s;
	cin >> n;
	vector<int> v;
	while(n--){
		int a;
		cin >> a;
		v.push_back(a);	
	}
	sort(v.begin(), v.end());
	for(int i = 0; i < v.size(); ++i){
		if(i == 0){
			s = v[i];
			d = 1;
			p = d;	
		}
		else{
			if(v[i] == s){
				if(d < p){
					++d;
				}
				else{
					++d;
					p = d;
				}	
			}
			else{
				d = 1;
				s = v[i];
			}
		}	
	}
	cout<<p<<endl;
	return 0;
}
