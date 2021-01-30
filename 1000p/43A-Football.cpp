#include <iostream>

using namespace std;

int main(){
	
	int n;
	
	cin >> n;
	
	string s, t1, t2;
	int g1 = 0, g2 = 0;
	
	for(int i = 0 ; i < n; ++i){
		cin >> s;
		if(i == 0){
			t1 = s;
			++g1;
		}
		else{
			if(s != t1){
				t2 = s;
				++g2;
			}
			else{
				++g1;
			}
		}
	}
	
	if(g1 > g2){
		cout<< t1 <<endl;
	}
	
	else{
		cout<< t2 <<endl;
	}
	
	return 0;
}
