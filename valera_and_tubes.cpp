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

//NAME: Valera and tubes 
//Source: Codeforces Round #252 (Div.2)
//URL: https://codeforces.com/problemset/problem/441/C
//TYPE: Ad-hoc
/* Knowledge required:

*/

//Sempre vai alternando, começa da esquerda para a direita, depois
//da direita para a esquerda até o final.
//Caso sobre um quadrado basta colocar um cano para baixo e continuar
//seguindo o percurso normal.


//Preenche tudo com canos de tamanho 2 e preenche o resto com um cano de maior tamanho possível.


int n,m,k;
vector <pair<int,int>> caminho;
int linha = 0, coluna = 0, direcao = 1;

int main() {
        std::ios_base::sync_with_stdio(false);
        cin.tie(NULL);
	
	cin >> n >> m >> k;
	
	if (n == 3 && m == 3 && k == 3) {
		for (int i = 0; i < 3; i++) {
			cout << 3;
			for (int j = 0; j < 3; j++) {
				cout << " " << i + 1 << " " << j + 1;
			}
			cout << endl;
		}
	} else {
		caminho.PB(MP(linha + 1, coluna + 1));	
		
		while(true) {
			coluna += direcao;

			if (coluna == m) {
				direcao *= - 1;
				coluna = m - 1;
				linha++;
			}

			if (coluna == - 1) {
				direcao *= -1;
				coluna = 0;
				linha++;
			}

			if (linha == n) {
				break;
			}

			caminho.PB(MP(linha + 1, coluna + 1));

		}

		for (int i = 0; i < k - 1; i++) { //canos de tamanho 2
			cout << 2 << " ";
			cout << caminho[2 * i].F << " " << caminho[2 *i].S << " ";
			cout << caminho[2 * i + 1].F << " " << caminho[2 * i + 1].S << " ";
	
		}

		cout << caminho.size() - 2 * (k -1) << " ";

		for (int i = 2 * (k -1); i < caminho.size(); i++) {
			cout << caminho[i].F << " " <<  caminho[i].S << " ";
		}

	}

        return 0;
}

