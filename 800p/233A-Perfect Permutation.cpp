#include <iostream>
using namespace std;

int main(){
	int n;
	cin >> n;
	int* p = new int[n]; 
	if(n % 2 == 1){
		cout<<-1<<endl;
	}
	else{
		for(int i = 0; i < n; i+=2){
			p[i] = i+2;
			p[i+1] = i+1;		
		}
		for(int i = 0; i < n; ++i){
			cout<<p[i]<<" ";
		}	
		cout<<endl;
	}
	return 0;
}
