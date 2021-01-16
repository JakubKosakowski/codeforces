#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int t;
	cin >> t;
	while(t--){
		int q = 0;
		vector<int> v;
		int p;
		cin >> p;
		if(p < 10){
			cout<<1<<endl;
			cout<<p<<endl;
		}
		else{
			if(p >= 1000){
				++q;
				int g = p%1000;
				v.push_back(p-g);
				p %= 1000;
			}
			if(p >= 100){
				++q;
				int g = p%100;
				v.push_back(p-g);
				p %= 100;
			}
			if(p >= 10){
				++q;
				int g = p%10;
				v.push_back(p-g);
				p %= 10;
			}
			if(p < 10 && p > 0){
				++q;
				v.push_back(p);
			}
			cout<<q<<endl;
			for(int i = 0; i < v.size(); ++i){
				cout<<v[i]<<" ";
			}
			cout<<endl;
		}
	}
	return 0;
}
