#include <iostream>
#include <vector>

using namespace std;

int main(){
	int w=0,b=0;
	string s;
	for(int i = 0; i < 8; ++i){
		getline(cin,s);
		for(char c:s){
			if(c == 'Q'){
				w+= 9;	
			}
			else if(c == 'N' || c == 'B'){
				w += 3;
			}
			else if(c == 'R'){
				w += 5;
			}
			else if(c == 'P'){
				++w;
			}
			else if(c == 'q'){
				b += 9;
			}
			else if(c == 'n' || c == 'b'){
				b += 3;
			}
			else if(c == 'r'){
				b += 5;
			}
			else if (c == 'p'){
				++b;
			}
		}
	}
	if(w > b){
		cout<<"White"<<endl;
	}
	else if(w < b){
		cout<<"Black"<<endl;
	}
	else{
		cout<<"Draw"<<endl;
	}
	
	return 0;
}
