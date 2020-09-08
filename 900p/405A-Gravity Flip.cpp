#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool myfunction(int i, int j) {
	return (i < j);
}

int main() {
	
	int n;
	vector<int> v;

	cin >> n;

	while (n--) {
		int c;
		cin >> c;
		v.push_back(c);
	}
	sort(v.begin(), v.end(), myfunction);

	for (int i = 0; i < v.size(); ++i) {
		cout << v[i] << " ";
	}

	return 0;
}
