# qr-code-generator

A QR code has several modes for encoding the data.

| Input mode   | Mode indicator | Max. characters | Possible characters, default encoding                      |
|--------------|----------------|-----------------|------------------------------------------------------------|
| Numeric only | 1              | 7,089           | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9                               |
| Alphanumeric | 2              | 4,296           | 0–9, A–Z (upper-case only), space, $, %, *, +, -, ., /, :  |
| Binary/byte  | 4              | 2,953           | ISO/IEC 8859-1                                             |
| Kanji/kana   | 8              | 1,817           | Shift JIS X 0208                                           |
| Structured Append   | 3              | unlimited           | Not specific              |

PS: structured append is a mode that the data is divided into several barcodes.

This repo demonstrates how to generate QR codes in different modes in Python with the segno library.

