#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
	
	int n, p, q;
	vector<int> v;

	cin >> n >> p;

	while(p--) {
		int x;
		cin >> x;
		v.push_back(x);
	}
	cin >> q;
	while (q--) {
		int x;
		cin >> x;
		v.push_back(x);
	}
	int d = 1;
	sort(v.begin(), v.end());
	
	for (int i = 0; i < v.size(); ++i) {
		if (v[i] == d) {
			++d;
		}
	}
	if (d-1 == n) {
		cout << "I become the guy." << endl;
	}
	else {
		cout << "Oh, my keyboard!" << endl;
	}

	return 0;
}
