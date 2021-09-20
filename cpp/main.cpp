#include <iostream>
#include <fstream>
#include <chrono>

using namespace std;
using namespace std::chrono;


int main() {
    auto start = high_resolution_clock::now();
    for (int i = 0; i < 10000000; ++i) {
        continue;
    }
    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<milliseconds>(stop - start);
    int elapsed = duration.count();

    cout << "Took: " << elapsed << " milliseconds" << endl;

    ofstream out;

    out.open("output.txt", std::ios_base::app);
    out << elapsed << "\n";
    out.close();
}