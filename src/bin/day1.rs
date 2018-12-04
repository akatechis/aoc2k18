use std::collections::HashSet;

fn main() {
  let input = include_str!("../data/day1.txt").lines()
  .map(|l| l.parse::<i32>().unwrap())
  .collect();

  part_1(&input);
  part_2(&input);
}

fn part_1 (input: &Vec<i32>) {
  let freq_a = input.iter().fold(0, |sum, i| sum + i);
  println!("Frequency = {}", freq_a);
}

fn part_2 (input: &Vec<i32>) {
  let mut first_dupe: Option<i32> = None;
  let mut frequencies: HashSet<i32> = HashSet::new();
  let mut freq_b: i32 = 0;
  frequencies.insert(freq_b);
  loop {
    for i in input {
      freq_b += i;
      if first_dupe.is_none() && frequencies.contains(&freq_b) {
        first_dupe = Some(freq_b);
      }
      frequencies.insert(freq_b);
    }

    if first_dupe.is_some() {
      break;
    }
  }
  println!("First duplicate frequency = {:?}", first_dupe);
}
