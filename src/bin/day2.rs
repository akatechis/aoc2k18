
use std::collections::HashMap;

fn count_char_occurences(string: &str) -> HashMap<char, usize> {
  let mut letters = HashMap::new();
  for ch in string.chars() {
    let counter = letters.entry(ch).or_insert(0);
    *counter += 1;
  }
  letters
}

fn count_repeat_chars (list: &Vec<String>, target_count: usize) -> usize {
  let mut count = 0;
  for id in list {
    let char_counts = count_char_occurences(&id);
    let counts: Vec<usize> = char_counts.values().map(|c| *c).collect();
    if counts.contains(&target_count) {
      count += 1;
    }
  }
  count
}

fn part_1 (input: &Vec<String>) {
  let count_2 = count_repeat_chars(input, 2);
  let count_3 = count_repeat_chars(input, 3);

  let chksum = count_2 * count_3;
  println!("Checksum = {}", chksum);
}

fn strings_are_close_enough (left: &String, right: &String) -> bool {
  let mut diffs = 0;

  for (ch_left, ch_right) in left.chars().zip(right.chars()) {
    if ch_left != ch_right {
      diffs += 1;
    }
  }

  diffs == 1
}

fn extract_common_chars (left: &String, right: &String) -> String {
  let mut common = String::with_capacity(left.len() - 1);

  for (ch_left, ch_right) in left.chars().zip(right.chars()) {
    if ch_left == ch_right {
      common.push(ch_left);
    }
  }

  common
}

fn part_2 (input: &Vec<String>) {
  for left in 0..input.len() {
    for right in left..input.len() {
      if left != right {
        let left_str = &input[left];
        let right_str = &input[right];
        if strings_are_close_enough(left_str, right_str) {
          let common_chars = extract_common_chars(left_str, right_str);
          println!("Found a match: ({}, {})", left_str, right_str);
          println!("Common characters: {}", common_chars);
        }
      }
    }
  }
}

fn main () {
  let input = include_str!("../data/day2.txt").lines().map(|l| l.to_owned()).collect();
  part_1(&input);
  part_2(&input);
}
