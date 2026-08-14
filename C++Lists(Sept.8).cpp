// Programming Languages | C++ Lists (Sept. 8)
// Imani Candler | 9.8.2024
// Objective: Create list of 32 random numbers. Print the list, sum, average, 
// the largest and smallest of the list, and the list in sorted order. 

#include <iostream>
#include <vector>
using namespace std;

int main(){

long int sum = 0;   
long int average = 0;
vector <int> random_vec;
for (int i = 0; i < 32; i++)
{
    random_vec.push_back(rand());
    sum = sum + random_vec[i];
    average = sum / 32;
}
    
cout << "Random list of numbers: " << endl;
for (int i = 0; i < 32; i++) // for loop generates vector of 32 values
{
    cout << random_vec[i] << endl; // displays random vector values
}

// use STL functions min_element and max_element to find min & max in range
auto min = min_element(random_vec.begin(), random_vec.end()); // finds the smallest value
auto max = max_element(random_vec.begin(), random_vec.end()); // finds the largest value
    
cout << "\n----- RESULTS BELOW -----" << endl;
cout << "The sum is: " << sum << endl;
cout << "The average is: " << average << endl; // the displayed average is correct, but are decimal points needed?
cout << "The smallest number in the list: " << *min << endl; // smallest 
cout << "The largest number in the list: " << *max << endl;

    
// The list in sorted order
cout << "The list in sorted order: " << endl;
sort (random_vec.begin(), random_vec.end()); // sorts the values from the beginning to end
    for (auto x : random_vec){ // automatically sorts values in vector "random_vec"
        cout << x << endl; // displays values in ascending order (low to high)
    }
      
return 0;
}









