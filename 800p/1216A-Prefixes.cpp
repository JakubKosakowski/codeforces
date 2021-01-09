#include <iostream>
#include <string>
using namespace std;

int main(){
	int t, ans = 0;
	string s;
	cin >> t >> s;
	for(int i = 0; i < t; i += 2){
		if(!((s[i] == 'a' && s[i+1] == 'b') || (s[i] == 'b' && s[i+1] == 'a'))){
			if(s[i] == 'a'){
				s[i] = 'b';
			}
			else{
				s[i] = 'a';
			}
			++ans;
		}
	}
	cout<<ans<<endl;
	cout<<s<<endl;
	return 0;
}
