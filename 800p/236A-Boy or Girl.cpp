#include <iostream>

using namespace std;

int main(){
	string s;
	
	cin >> s;
	
	int ans=0;
	for(int i = 0; i < s.length(); ++i){
		int g=0;
		for(int j = i+1; j < s.length(); ++j){
			if(s[i] == s[j]){
				++g;
			}
		}
		if(g == 0){
			++ans;
		}
	}
	
	if(ans % 2 == 0){
		cout<<"CHAT WITH HER!"<<endl;
	}
	else{
		cout<<"IGNORE HIM!"<<endl;
	}
	
	return 0;
}
