#include <iostream>

using namespace std;

int main(){
	
	long long n,m,a;
	
	cin >> n >> m >> a;
	
	if(a == 1){
		cout<< n * m <<endl;
	}
	else{
		long long g = 1, b = 1;
		
		n -= a;
		m -= a;
		
		while(n > 0){
			++g;
			n -= a;
		}
		
		while(m > 0){
			++b;
			m -= a;
		}
		
		cout<<g*b<<endl;
	}
	return 0;
}
