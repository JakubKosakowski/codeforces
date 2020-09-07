#include <iostream>
#include <cstdlib>
#include <vector>

using namespace std;

int main() {
	
	int t;

	cin >> t;
	vector<int> v1, v2;

	string a, b;

	cin >> a >> b;
	for (char c : a) {
		int g = int(c);
		v1.push_back(g);
	}
	for (char c : b) {
		int g = int(c);
		v2.push_back(g);
	}
	
	int ans = 0;
	for (int i = 0; i < t; ++i) {
		int x = v1[i], y = v2[i];
		if (abs(x - y) <= 5) {
			ans += abs(x - y);
		}
		else {
			ans += (10 - abs(x - y));
		}
	}
	cout << ans << endl;


	return 0;
}
