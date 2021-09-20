use std::fs;
use std::io::prelude::*;
use std::time::{Instant};

fn main() {
  let start = Instant::now();
  for _ in 0..10_000_000 {
    continue;
  }
  let elapsed = start.elapsed().as_millis();
  println!("Took: {:?} milliseconds", elapsed);

  let data = format!("{:?}", elapsed);
  let mut file = fs::OpenOptions::new()
      .write(true)
      .create(true)
      .append(true)
      .open("output.txt")
      .unwrap();

  if let Err(e) = writeln!(file, "{}", data) {
    eprintln!("Couldn't write to file: {}", e);
  }
}