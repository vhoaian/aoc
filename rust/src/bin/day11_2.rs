use std::fs;
use std::path::{Path};


fn get_input(p: &str) -> String {
    let file_path = Path::new(".").join("inputs").join(p);
    let contents = fs::read_to_string(file_path)
        .expect("Should have been able to read the file");
    contents
}

fn translate_1d_to_2d_idx(idx: u32, width: u32) -> (u32, u32) {
    (idx / width, idx % width)
}

fn translate_2d_to_1d_idx(x: u32, y: u32, width: u32) -> u32 {
    x * width + y
}

fn get_c_from_x_y(chars: &Vec<char>, width: u32, x: u32, y: u32) -> &char {
    let idx = translate_2d_to_1d_idx(x, y, width);
    chars.get(idx as usize).expect("Idx error")
}

fn find_expanded(chars: &Vec<char>, width: u32, height: u32, find_on_x: bool) -> Vec<u32> {
    let mut result: Vec<u32> = vec![];
    let (a, b) = if find_on_x { (height, width) } else { (width, height) };
    for i in 0..a {
        let mut is_expanded = true;
        for j in 0..b {
            if (chars[translate_2d_to_1d_idx(i, j, width) as usize] != '.' && find_on_x)
                || (chars[translate_2d_to_1d_idx(j, i, width) as usize] != '.' && !find_on_x) {
                is_expanded = false;
                break;
            }
        }
        if is_expanded {
            result.push(i);
        }
    }
    result
}

fn cal_distance(galaxy_idx_1: u32, galaxy_idx_2: u32, expanded_in_x: &Vec<u32>, expanded_in_y: &Vec<u32>, width: u32) -> u64 {
    let (mut galaxy_1_x, mut galaxy_1_y) = translate_1d_to_2d_idx(galaxy_idx_1, width);
    let (mut galaxy_2_x, mut galaxy_2_y) = translate_1d_to_2d_idx(galaxy_idx_2, width);
    if galaxy_1_x < galaxy_2_x {
        let t = galaxy_1_x;
        galaxy_1_x = galaxy_2_x;
        galaxy_2_x = t;
    }
    if galaxy_1_y < galaxy_2_y {
        let t = galaxy_1_y;
        galaxy_1_y = galaxy_2_y;
        galaxy_2_y = t;
    }

    let mut distance_in_x: u64 = (galaxy_1_x - galaxy_2_x) as u64;
    let mut distance_in_y: u64 = (galaxy_1_y - galaxy_2_y) as u64;

    for x in expanded_in_x {
        if x <= &galaxy_1_x && x >= &galaxy_2_x {
            distance_in_x += 1000000 - 1;
        }
    }

    for y in expanded_in_y {
        if y <= &galaxy_1_y && y >= &galaxy_2_y {
            distance_in_y += 1000000 - 1;
        }
    }

    return distance_in_x + distance_in_y;
}

fn main() {
    let inp = get_input("day11_1_2.inp");
    let height = inp.lines().count() as u32;
    let width = inp.lines().nth(0).unwrap().len() as u32;

    let mut chars = inp.lines().map(|x| x.chars().collect::<Vec<char>>()).flatten().collect::<Vec<char>>();

    let expanded_in_x: Vec<u32> = find_expanded(&chars, width, height, true);
    let expanded_in_y: Vec<u32> = find_expanded(&chars, width, height, false);

    let galaxy_idx: Vec<u32> = chars.iter().enumerate()
        .filter(|(a, &b)| b == '#')
        .map(|(i, _)| i as u32).collect();


    let mut sum = 0;

    for i in 0..(galaxy_idx.len() - 1) {
        for j in (i + 1)..galaxy_idx.len() {
            sum += cal_distance(galaxy_idx[i], galaxy_idx[j], &expanded_in_x, &expanded_in_y, width);
            // println!("Distance from {} to {} is {}", i + 1, j + 1, cal_distance(galaxy_idx[i], galaxy_idx[j], &expanded_in_x, &expanded_in_y, width));
        }
    }

    println!("{}", sum);
}