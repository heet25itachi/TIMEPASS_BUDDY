#include <iostream>
#include <string>
#include <vector>
#include <iomanip> // Needed for cleaner output

using namespace std;

// --- Function to perform XOR encryption/decryption ---
// Takes constant references to data and key for efficiency
string xor_cipher(const string& data, const string& key) {
    // If the key is empty, return data unchanged to prevent division by zero
    if (key.empty()) {
        return data;
    }

    string output = data;
    int key_len = key.length();

    for (size_t i = 0; i < data.length(); ++i) {
        // Apply XOR operation byte-by-byte, cycling through the key
        // key[i % key_len] ensures the key repeats if it's shorter than the data
        output[i] = data[i] ^ key[i % key_len];
    }
    return output;
}

int main() {
    cout << "--- Symmetric Cipher (XOR) Demonstration ---" << endl;
    
    string original_text = "The quick brown fox jumps over the lazy dog.";
    // Corrected variable name: key_t was used in the user's prompt but 'key' is cleaner
    string key = "SECRETKEY";
    
    cout << "Original Text: " << original_text << endl;
    cout << "Key:           " << key << endl;

    // 1. Encryption
    string ciphertext = xor_cipher(original_text, key);
    
    cout << "\nCiphertext (Raw Bytes): ";
    for (char c : ciphertext) {
        // Outputting non-printable characters as their ASCII integer value
        // Using setw(3) and setfill('0') for consistent formatting
        cout << setfill('0') << setw(3) << (int)(unsigned char)c << " ";
    }
    cout << endl;

    // 2. Decryption
    // XORing again with the same key reverses the process
    string decrypted_text = xor_cipher(ciphertext, key);
    cout << "\nDecrypted Text: " << decrypted_text << endl;

    // 3. Verification
    if (original_text == decrypted_text) {
        cout << "\n[SUCCESS] Encryption and decryption verified." << endl;
    } else {
        cout << "\n[FAIL] Decryption mismatch." << endl;
    }

    return 0;
}
