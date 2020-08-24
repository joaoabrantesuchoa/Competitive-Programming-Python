/* Headers */

#include <bits/stdc++.h>

using namespace std;

const long long MOD = 1e9 + 7;
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef pair<int,pii> iii;
typedef vector<pii> vii;
typedef vector<vi> vvi;
typedef priority_queue<pii, vector<pii>, greater<pii>> fila_prioridade;
typedef priority_queue<iii, vector<iii>, greater<iii>> fila_prioridade_grids;


#define INF 1000000000
#define F first
#define S second
#define PB push_back
#define MP make_pair
#define REP(i,a,b) for (int i = a; i <= b; i++)


/* -------------- */

//NAME: Number of ways
//Source: Codeforces Round #2 (Div.2)
//URL: https://codeforces.com/problemset/problem/466/C
//TYPE: two pointers
/* Knowledge required:

*/

int n;
ll numeros[500009];
ll ways = 0, total = 0, prefix_sum = 0, subarrays_validas = 0;


int main() {
        std::ios_base::sync_with_stdio(false);
        cin.tie(NULL);

	cin >> n;

	for (int i = 0; i < n; i++) {
		cin >> numeros[i];
		total += numeros[i];
	}

	if (total % 3 != 0) { //Caso a soma não seja divísivel por 3, também não é possível dividir em três subarrays 
		cout << 0 << "\n";
	} else {
		total = total / 3;
		for(int i = 0; i < n - 1; i++) {
			prefix_sum += numeros[i];
			if (prefix_sum == total * 2) { //Caso seja válida significa que existe subarrays_validas modos de dividir a array em três partes sendo a primeira o intervalo [0,i].
				ways += subarrays_validas;
			} 

			if (prefix_sum  == total) {
				subarrays_validas++;
			}
		}

		cout << ways << endl;

	}
        return 0;
}

