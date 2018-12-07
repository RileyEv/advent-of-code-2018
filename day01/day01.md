
Day 01
======

Some required imports:
```lhs 

> import Text.Yoda
> import Data.Char
> import Magic

```

Task 1
------

We have the frequency language defined by the following grammar:

```

frequency ::= "+" <number> <frequency>
            | "-" <number> <frequency>
            | ϵ

```


Here is the associated datatype:

```lhs 

> data Frequency = Add Int Frequency
>                | Sub Int Frequency
>                | Epsilon
>                deriving Show

```

Here is the associated parser for the language

```lhs

> digits :: Parser String
> digits = cull(some (satisfy isDigit))

> number :: Parser Int
> number = read <$> digits

> frequency :: Parser Frequency
> frequency = cull (Add     <$ token "+" <*> number <* token "" <*> frequency
>               <|> Sub     <$ token "-" <*> number <* token "" <*> frequency
>               <|> Epsilon <$ pure ())

```

Here is the evaluation function for Frequency

```lhs

> evalFrequency :: Frequency -> Int
> evalFrequency (Add x f) = x + evalFrequency f
> evalFrequency (Sub x f) = evalFrequency f - x
> evalFrequency (Epsilon) = 0

```

Here is the main function

```lhs

> main :: IO ()
> main = do
>    s <- readFile "day01-1-input.txt"
>    putStrLn (show (evalFrequency(fst ((parse frequency s)!!0))))

```



