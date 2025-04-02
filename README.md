# Hill Cipher Variants

This repository contains Python implementations of the Hill cipher and its recursive variant, using matrix operations for encryption and decryption.

## Files Overview

### 1. hill_sh.py
- **Algorithm**: Classic Hill Cipher
- **Description**:
  - Implements the standard Hill cipher using matrix multiplication
  - Requires a single key that must be a perfect square in length (4, 9, 16, etc. characters)
  - Key matrix must be invertible modulo 26 (determinant coprime with 26)
  - Automatically pads plaintext with 'a' (0) if length isn't multiple of matrix dimension

### 2. rec_hill_sh.py
- **Algorithm**: Recursive Hill Cipher (dual-key variant)
- **Description**:
  - Extends the Hill cipher with two initial key matrices that recursively generate new keys
  - Each block of plaintext uses a different key derived from previous keys
  - Maintains same mathematical requirements as basic Hill cipher but with evolving keys
  - Provides stronger security than basic Hill cipher through key recursion

## Usage Instructions

### For both scripts:
1. Clone the repository or download the files
2. Run the desired script: `python filename.py`
3. Follow the on-screen prompts to enter text and keys

### Key Requirements:
- **hill_sh.py**:
  - Single key string (e.g., "dcba")
  - Key length must be a perfect square (4, 9, 16, etc.)
  - Resulting matrix must have determinant coprime with 26

- **rec_hill_sh.py**:
  - Two initial key strings of same length
  - Both keys must satisfy same requirements as basic Hill cipher
  - Both keys must produce matrices of same dimension

## Technical Notes
- Both implementations work with lowercase English alphabet only
- Non-alphabetic characters will cause errors
- The recursive variant provides enhanced security through key evolution
- Includes extensive error checking for key validity
- Uses NumPy for efficient matrix operations
- Implements modular arithmetic for all matrix operations
