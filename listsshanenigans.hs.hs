
fatorial :: Int -> Int
fatorial 0=1
fatorial n = n * fatorial (n-1)


somal :: [Int] -> Int
somal [] = 0 --base
somal (x:xs) = x + somal xs


tam :: [Int] -> Int
tam [] = 0
tam (x:xs) = 1 + tam (xs)

mut :: [ Int] -> Int
mut [] = 1
mut (x:xs) = 1 * mut (xs)
