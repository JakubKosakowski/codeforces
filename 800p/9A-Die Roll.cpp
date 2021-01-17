#include <iostream>

using namespace std;

int main(){
	int y,w,max,d=0;
	cin>>y>>w;
	if(y > w){
		max = y;
	}
	else{
		max = w;
	}
	for(int i = max; i <= 6; ++i){
		++d;
	}
	if(d == 1){
		cout<<"1/6"<<endl;
	}
	else if(d == 2){
		cout<<"1/3"<<endl;
	}
	else if(d == 3){
		cout<<"1/2"<<endl;
	}
	else if(d == 4){
		cout<<"2/3"<<endl;
	}
	else if(d == 5){
		cout<<"5/6"<<endl;
	}
	else{
		cout<<"1/1"<<endl;
	}
	return 0;
}
