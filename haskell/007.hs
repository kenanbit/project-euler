#!/usr/bin/runhaskell
{-|

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

-}

import Data.List
import PEFunctions

main = do
    putStrLn . show $ primes !! 10000
