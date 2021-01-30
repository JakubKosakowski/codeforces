#include <iostream>
#include <cctype>

using namespace std;

int main(){
	
	string s;
	
	cin >> s;
	
	if(isupper(s[0])){
		int u = 1;
		
		for(int i = 1; i < s.length(); ++i){
			if(isupper(s[i])){
				++u;
			}
		}	
		if(u == s.length()){
			for(int i = 0; i < s.length(); ++i){
				s[i] = tolower(s[i]);
			}
			cout<<s<<endl;
		}
		else{
			cout<<s<<endl;
		}
	}
	else{
		int l = 0;
		
		for(int i = 0; i < s.length(); ++i){
			if(islower(s[i])){
				++l;	
			}
		}
		if(l == 1){
			for(int i = 0; i < s.length(); ++i){
				if(i == 0){
					if(isupper(s[i]) != 1){
						s[i] = toupper(s[i]);
					}	
				}
				else{
					if(islower(s[i]) != 1){
						s[i] = tolower(s[i]);
					}
				}
			}
			cout<<s<<endl;
		}
		else{
			cout<< s <<endl;
		}	
	}
	return 0;
}
