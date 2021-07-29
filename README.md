# Borderless - Comic Border Remover

Removes excessive borders from CBZ and CBR files

## Installation

```
git clone https://github.com/Demoli/borderless.git
cd borderless
pip install -r requirements.txt
``` 

## Requirements

Python 3.6+

## Usage

Can accept both CBZ and CBR files as input but output will always be CBZ 

`python main.py [input file path.cbz] [output file path.cbz]`

### Options

* --margin - Keep a specified number of pixels as a border, default 20