#include <sstream>
#include <fstream>
#include <vector>
#include <string>
#include "utils.h"

using namespace std;

string joinStr(vector<string> elements, const char* delimiter) {
    ostringstream oss;
    auto iter = begin(elements);

    if (iter != end(elements)) {
        oss << *iter;
        ++iter;
    }

    for (; iter != end(elements); ++iter) {
        oss << delimiter << *iter;
    }

    return oss.str();
}

vector<string> getInput(const char* fileName) {
    vector<string> lines;

    if (ifstream file(fileName); file.is_open()) {
        string line;
        while (getline(file, line)) {
            lines.push_back(line);
        }
        file.close();
    } else {
        throw runtime_error("Could not open input file!");
    }

    return lines;
}
