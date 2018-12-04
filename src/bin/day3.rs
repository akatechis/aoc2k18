
use std::collections::HashMap;

type Fabric = HashMap<(usize, usize), TileClaim>;

#[derive(Debug, PartialEq)]
enum TileClaim {
  Claimed,
  Conflict
}

#[derive(Debug)]
struct Claim {
  id: String,
  origin: (usize, usize),
  size: (usize, usize)
}

fn parse_claim (input: &str) -> Claim {
  let mut tokens = input.split_whitespace();
  let id = tokens.next().unwrap()[1..].to_owned();

  tokens.next();

  let origin = {
    let mut origin_tokens = tokens.next().unwrap().split(',');
    let origin_x = origin_tokens.next().unwrap().parse::<usize>().unwrap();
    let origin_y_str = origin_tokens.next().unwrap();
    let origin_y = origin_y_str[..origin_y_str.len() - 1].parse::<usize>().unwrap();
    (origin_x, origin_y)
  };

  let size = {
    let mut size_tokens = tokens.next().unwrap().split('x');
    let w = size_tokens.next().unwrap().parse::<usize>().unwrap();
    let h = size_tokens.next().unwrap().parse::<usize>().unwrap();
    (w, h)
  };

  Claim {
    id, origin, size
  }
}

fn claim_tile (fabric: &mut Fabric, tile: (usize, usize)) {
  if !fabric.contains_key(&tile) {
    fabric.insert(tile, TileClaim::Claimed);
  } else {
    // tile has already been claimed, just set it to be conflicted.
    fabric.insert(tile, TileClaim::Conflict);
  }
}

fn apply_claims (
  mut fabric: &mut Fabric,
  claims: &Vec<Claim>
) {
  for claim in claims {
    let (x, y) = claim.origin;
    let (w, h) = claim.size;
    for tile_x in x..x+w {
      for tile_y in y..y+h {
        claim_tile(&mut fabric, (tile_x, tile_y));
      }
    }
  }
}

fn part_2 (claims: &Vec<Claim>) {
  let mut fabric = HashMap::new();

  apply_claims(&mut fabric, claims);

  for claim in claims {
    let (x, y) = claim.origin;
    let (w, h) = claim.size;
    let mut conflicted = false;
    for tile_x in x..x+w {
      if !conflicted {
        for tile_y in y..y+h {
          if fabric.get(&(tile_x, tile_y)).unwrap() == &TileClaim::Conflict {
            conflicted = true;
            break;
          }
        }
      }
    }
    if !conflicted {
      println!("Claim has no conflicts: {:?}", claim);
    }
  }
}

fn part_1 (claims: &Vec<Claim>) {
  let mut fabric = HashMap::new();

  apply_claims(&mut fabric, &claims);

  let conflicted_tiles = fabric.values()
    .filter(|t| **t == TileClaim::Conflict)
    .count();

  println!("Number of conflicted tiles: {}", conflicted_tiles);
}

fn main () {
  let claims: Vec<Claim> = include_str!("./day3.txt").lines().map(parse_claim).collect();
  part_1(&claims);
  part_2(&claims);
}
