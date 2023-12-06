#ifndef CPP_UTILS_H
#define CPP_UTILS_H
#include <vector>
#include <string>

using namespace std;

string joinStr(const vector<string> elements, const char* delimiter);

vector<string> getInput(const char* fileName);
#endif
