This module has some magic stuff made on previous work sheets that are needed for the next worksheets

```lhs

> module Magic
>   ( whitespace
>   , token
>   ) where

```

We need some Yoda shit
```lhs 

> import Text.Yoda

```

Here is some magic string reader
```lhs

> whitespace :: Parser ()
> whitespace = skip (many (oneOf [' ', '\t', '\n']))

> token :: String -> Parser String
> token t = string t <* whitespace

```
