# Simple Text Encoder/Decoder

A pair of Python scripts for basic text encoding and decoding. The encoder transforms input text by inserting random characters between each original character, while the decoder reverses this process to recover the original message.

## Files
- `encoder.py` - Adds random characters to text
- `decoder.py` - Removes added characters to decode text

## How It Works
**Encoding**: Takes input text and inserts 5 random letters after each character
**Decoding**: Removes every 6th character to reconstruct original text

## Usage
Run encoder: `python encoder.py` - enter text to encode
Run decoder: `python decoder.py` - enter encoded text to decode

## Note
Basic educational implementation - not cryptographically secure. Useful for understanding simple encoding concepts.
