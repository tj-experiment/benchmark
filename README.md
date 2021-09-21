# speed_test
Iterate over `10_000_000` items and recorded execution time for each language.

Fastest: 
- `Cython`: `0.0021949999999965053` milliseconds
- `C`: `0.026882` milliseconds

![Screen Shot 2021-09-21 at 10 06 03 AM](https://user-images.githubusercontent.com/17484350/134186722-7f469101-e1dd-4536-a7a5-a0e7ab964eea.png)

Average:
- `GoLang`: `4` milliseconds
- `PyPy2`: `12.2358798981` milliseconds
- `PyPy3`: `13.275389967020601` milliseconds
- `Node`: `23.389706` milliseconds
- `C++`: `23` milliseconds
- `Scala`: `68` milliseconds

![Screen Shot 2021-09-21 at 10 09 50 AM](https://user-images.githubusercontent.com/17484350/134186724-2956e2df-ec3f-464e-a149-0920bcd5986d.png)

Slowest:
- `Elixir`: `320.48` milliseconds
- `Rust`: `440` milliseconds
- `Python`: `488.528394` milliseconds
- `Ruby`: `795.4700002446771` milliseconds

![Screen Shot 2021-09-21 at 10 11 08 AM](https://user-images.githubusercontent.com/17484350/134186726-5e385e25-8c7d-48a2-8e64-56203ba85c76.png)
