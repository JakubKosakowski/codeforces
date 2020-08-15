#include <iostream>
#include <string>

using namespace std;

int main() {
	int n, m;
	string ans;

	cin >> n >> m;

	for (int i = 0; n != 0 && m != 0; ++i) {
		if (i % 2 == 0) {
			ans = "Akshat";
			--n;
			--m;
		}
		else if(i % 2 == 1){
			ans = "Malvika";
			--n;
			--m;
		}
	}
	cout << ans << endl;
	return 0;
}
