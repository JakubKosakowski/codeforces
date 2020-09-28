#include <bits/stdc++.h>

using namespace std;

int main()
{
    int a, b, c, d, vp, mp;

    cin >> a >> b >> c >> d;

    vp = max((3 * b / 10), b - (b / 250) * d);
    mp = max((3 * a / 10), a - (a / 250) * c);

    if (vp > mp) {
        cout << "Vasya" << endl;
    }
    else if (vp < mp) {
        cout << "Misha" << endl;
    }
    else {
        cout << "Tie" << endl;
    }

    return 0;
}
