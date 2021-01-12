#include <iostream>
#include <vector>
using namespace std;

int main(){
	string s;
	int k, l;
	cin >> s >> k;
	vector<string> v{"January","February","March","April","May","June","July","August","September","October","November","December"};
	for(int i = 0; i < v.size(); ++i){
		if(s == v[i]){
			l = i+1;
		}
	}
	l += k;
	while(l > 12){
		l -= 12;
	}
	cout<<v[l-1]<<endl;
	return 0;
}
