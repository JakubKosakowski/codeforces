#include <iostream>

using namespace std;

int main(){
	int a,b,c,d=0,wa=0,wb=0,i=0;
	cin>>a>>b;
	
	if(a > b){
		c = a-b;
		if(c % 2 == 0){
			++d;
			while(i<b+(c/2)-1){
				++wb;
				++i;
			}
			++i;
			while(i<6){
				++wa;
				++i;
			}
			cout<<wa<<" "<<d<<" "<<wb;
		}
		else{
			while(i<b+(c/2)){
				++wb;
				++i;
			}
			while(i<6){
				++wa;
				++i;
			}
			cout<<wa<<" "<<d<<" "<<wb;
		}
	}
	else if(a < b){
		c = b-a;
		if(c % 2 == 0){
			++d;
			while(i<a+(c/2)-1){
				++wa;
				++i;
			}
			++i;
			while(i<6){
				++wb;
				++i;
			}
			cout<<wa<<" "<<d<<" "<<wb;
		}
		else{
			while(i<a+(c/2)){
				++wa;
				++i;
			}
			while(i<6){
				++wb;
				++i;
			}
			cout<<wa<<" "<<d<<" "<<wb;
		}
	}
	else if (a == b){
		d = 6;
		cout<<wa<<" "<<d<<" "<<wb;
	}
	return 0;
}
