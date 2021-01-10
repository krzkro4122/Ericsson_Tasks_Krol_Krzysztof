/*#include <iostream>
#include <string>

using namespace std;

// Function converting decimal numbers to binary
string dec_to_bin(int decimal) {

	char binary[255] = "";
	_itoa_s(decimal, binary, 2);

	return (string)binary;
}

// Function converting binary numbers to decimal
int bin_to_dec(string binary) {

	int decimal = strtol(binary.c_str(), NULL, 2);

	return decimal;
}

int main() {

	int mode = 0;

	while( true ){
		// Welcome Menu
		cout << "Welcome to Binary-Decimal Converter!" << endl;
		cout << "Choose conversion mode by entering following digits: " << endl;
		cout << "1. Binary => Decimal" << endl;
		cout << "2. Decimal => Binary" << endl;
		cout << "3. Exit" << endl;

		cin >> mode;

		// Exit
		if (mode == 3) {
			cout << "Thank you for your time!" << endl;
			break;
		}

		string number = "";

		// Binary => Decimal
		if ( mode == 1 ) {

			cout << "Binary to Decimal (1st) mode selected. " << endl;
			cout << "Input numbers continuosly: (enter 'exit' to return to the Welcome menu)" << endl;

			bool is_binary = true;

			while ( true ) {

				cin >> number;

				if (number == "exit")
					break;

				// Check if input is a binary number
				for (int i = 0; i < number.length(); i++) {
					if (number[i] == '1' || number[i] == '0')
						continue;
					is_binary = false;
					break;
				}

				// Omit output if number is not binary
				if (!is_binary) {
					cout << "Bad input detected! Try again:" << endl;
					// Reset is_binary flag 
					is_binary = true;
					continue;
				}

				cout << number << " => " << bin_to_dec(number) << endl;
			}
		}
		// Decimal => Binary
		else if ( mode == 2 ) {

			cout << "Decimal to Binary (2nd) mode selected. " << endl;
			cout << "Input numbers continuosly: (enter 'exit' to return to the Welcome menu)" << endl;

			bool is_number = true;
			int number_int = 0;

			while (true) {

				cin >> number;

				if (number == "exit")
					break;

				char digits[] = { '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' };

				for (int i = 0; i < number.length(); i++) {
					if (find(begin(digits), end(digits), number[i]) != end(digits)) {
						continue;
					}	
					is_number = false;
					break;
				}

				// Omit stoi() and output if input is not a number
				if (!is_number) {
					cout << "Bad input detected! Try again:" << endl;
					// Reset is_number flag
					is_number = true;
					continue;
				}
				else {
					number_int = stoi(number);

					cout << number_int << " => " << dec_to_bin(number_int) << endl;
				}
			}
		}
		// Wrong Input Handler
		else {
			cout << "Bad input detected! Try again:" << endl;
			continue;
		}
		system("CLS");
	}

	return 0;
}
*/