#include <iostream>
#include <vector>

using namespace std;

int main() {
	int a, sum = 0, i = 0;
	vector<int> v = { 100,20,10,5,1 };

	cin >> a;

	while (a > 0) {
		if (v[i] <= a) {
			++sum;
			a -= v[i];
		}
		else {
			++i;
		}
	}
	cout << sum << endl;

	return 0;
}
