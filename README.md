# speed_test
Iterate over `10_000_000` items and recorded execution time for each language.

Fastest: 
- `Cython`: `0.0012919999999999598` milliseconds
- `C`: `0.023278` milliseconds

![Screen Shot 2021-09-21 at 10 06 03 AM](https://user-images.githubusercontent.com/17484350/134186722-7f469101-e1dd-4536-a7a5-a0e7ab964eea.png)

Average:
- `Scala`: `1` milliseconds
- `GoLang`: `3` milliseconds
- `PyPy2`: `11.7371082306` milliseconds
- `PyPy3`: `12.248411017935723` milliseconds
- `Node`: `22.435445` milliseconds
- `C++`: `23` milliseconds

![Screen Shot 2021-09-21 at 10 09 50 AM](https://user-images.githubusercontent.com/17484350/134186724-2956e2df-ec3f-464e-a149-0920bcd5986d.png)

Slowest:
- `Elixir`: `289` milliseconds
- `Rust`: `289` milliseconds
- `Python`: `291.02987700000006` milliseconds
- `Ruby`: `447` milliseconds

![Screen Shot 2021-09-21 at 10 11 08 AM](https://user-images.githubusercontent.com/17484350/134186726-5e385e25-8c7d-48a2-8e64-56203ba85c76.png)
