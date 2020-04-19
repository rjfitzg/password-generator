# Password Generator

## Information
This is a python based command line tool used to generate a password using random characters or a supplied dictionary file.

## Example commands

### Help
Will list out all available commands and sample usage.

#### Base usage
`password.py --help`

`password.py -h`

### Random password
Will generate a password using random letters, numbers and symbols of the supplied length. Will default to 20 characters if no length is supplied. 

#### Base usage
`password.py --random`

`password.py -r`

#### With supplied length
`password.py --count 30 --random`

`password.py -c 30 -r`

### Dictionary based password
Will generate a password using random words from a supplied dictionary of the supplied length. Will default to internal dictionary if none is suppled. Will default to 3 words if none is supplied. Options for adding leading symbol to the password and seperator between words within the password. 

#### Base usage
`password.py --dictionary`

`password.py -d`

#### With supplied length
`password.py --count 4 --dictionary`

`password.py -c 4 -d`

#### With supplied dictionary
`password.py --file /path --dictionary`

`password.py -f /path -d`

#### With leading symbol
`password.py --leadingSymbol --dictionary`

`password.py -l -d`

#### With seperator
`password.py --seperator --dictionary`

`password.py -d -d`
