#include <iostream>
#include <vector>

using namespace std;

int main() {
	int a, ans = 0;
	vector<int> v;

	cin >> a;

	for (int i = 0; i < a; ++i) {
		long long x;
		cin >> x;
		v.push_back(x);
	}
	if (a == 1) {
		cout << 0 << endl;
	}
	else {
		int ind = 0;
		long long max = v[0];
		for (int i = 1; i < v.size(); ++i) {
			if (v[i] > max) {
				max = v[i];
				ind = i;
			}
		}

		for (int i = 0; i < v.size(); ++i) {
			if (i != ind) {
				long long d = v[i];
				while (d != max) {
					++ans;
					++d;
				}
			}
		}
		cout << ans << endl;
	}
	return 0;
}
