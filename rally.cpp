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

//NAME: Rally
//Source:  Atcoder Beginner Contest 156
//URL: https://atcoder.jp/contests/abc156/tasks/abc156_c
//TYPE: Ad-hoc
/* Knowledge required:

*/

//A quantidade de ponto e o tamanho deles é muito pequeno, então é possível fazer
//uma força bruta e ir guardando o menor valor.

int coordenadas[105];
ll n,stamina;
ll resp = 10000000;

int main() {
        std::ios_base::sync_with_stdio(false);
        cin.tie(NULL);
	
	cin >> n;

	for (int i = 0; i < n; i++) {
		cin >> coordenadas[i];
	}

	for (int p = 1; p <= 200; p++) {
		stamina = 0;
		for (int i = 0; i < n; i++) {
			stamina += pow((coordenadas[i] - p), 2);
		}

		if (stamina < resp) {
			resp = stamina;
		}
	}
	cout << resp << endl;



        return 0;
}

