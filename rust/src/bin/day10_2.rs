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

fn find_start_idx(chars: &Vec<char>, width: u32) -> (u32, u32) {
    let idx_1d = chars.iter().position(|&x| x == 'S').expect("Must have a start point");
    translate_1d_to_2d_idx(idx_1d as u32, width)
}

fn get_c_from_x_y(chars: &Vec<char>, width: u32, x: u32, y: u32) -> &char {
    let idx = translate_2d_to_1d_idx(x, y, width);
    chars.get(idx as usize).expect("Idx error")
}

fn find_directions(c: char) -> Vec<char> {
    match c {
        '|' => vec!['N', 'S'],
        '-' => vec!['E', 'W'],
        'L' => vec!['N', 'E'],
        'J' => vec!['N', 'W'],
        '7' => vec!['S', 'W'],
        'F' => vec!['S', 'E'],
        _ => vec![],
    }
}

fn translate_d_to_loc(c: char) -> &'static (i32, i32) {
    match c {
        'N' => &(-1, 0),
        'S' => &(1, 0),
        'W' => &(0, -1),
        'E' => &(0, 1),
        _ => todo!()
    }
}

fn find_next_loc(chars: &mut Vec<char>, nums: &Vec<i32>, width: u32, height: u32, x: u32, y: u32) -> Vec<(u32, u32)> {
    let mut c = *get_c_from_x_y(chars, width, x, y);

    if c == 'S' {
        let mut direction = String::new();
        if x > 0 && ['7', '|', 'F'].contains(get_c_from_x_y(chars, width, x - 1, y)) {
            direction.push('N');
        }
        if x < height - 1 && ['L', '|', 'J'].contains(get_c_from_x_y(chars, width, x + 1, y)) {
            direction.push('S');
        }
        if y > 0 && ['L', '-', 'F'].contains(get_c_from_x_y(chars, width, x, y - 1)) {
            direction.push('W');
        }
        if y < width - 1 && ['7', '-', 'J'].contains(get_c_from_x_y(chars, width, x, y + 1)) {
            direction.push('E');
        }
        if direction == "NS" {
            c = '|';
        } else if direction == "WE" {
            c = '-';
        } else if direction == "NW" {
            c = 'J';
        } else if direction == "NE" {
            c = 'L';
        } else if direction == "SW" {
            c = '7';
        } else {
            c = 'F';
        }
        chars[translate_2d_to_1d_idx(x, y, width) as usize] = c;
    }

    let available_directions: Vec<(i32, i32)> = find_directions(c).iter().map(|&x| *translate_d_to_loc(x)).collect();


    let mut result: Vec<(u32, u32)> = vec![];
    for (dx, dy) in available_directions {
        let (new_x, new_y) = (x as i32 + dx, y as i32 + dy);
        if new_x >= 0 && (new_x as u32) < height && new_y >= 0 && (new_y as u32) < width {
            let new_in_1d = translate_2d_to_1d_idx(new_x as u32, new_y as u32, width) as usize;
            if chars[new_in_1d] != '.' && nums[new_in_1d] == -1 {
                result.push((new_x as u32, new_y as u32));
            }
        }
    }
    result
}

fn find_ways(chars: &mut Vec<char>, nums: &mut Vec<i32>, width: u32, height: u32) -> i32 {
    let (start_x, start_y) = find_start_idx(chars, width);
    nums[translate_2d_to_1d_idx(start_x, start_y, width) as usize] = 0;

    let mut queue = find_next_loc(chars, nums, width, height, start_x, start_y);
    queue.iter().for_each(|&(x, y)| nums[translate_2d_to_1d_idx(x, y, width) as usize] = 1);

    while !queue.iter().all(|&x| x == queue[0]) {
        let (cur_x, cur_y) = queue.remove(0);
        let count = nums[translate_2d_to_1d_idx(cur_x, cur_y, width) as usize];
        let new_point = find_next_loc(chars, nums, width, height, cur_x, cur_y);
        new_point.iter().for_each(|&(x, y)| nums[translate_2d_to_1d_idx(x, y, width) as usize] = count + 1);
        queue.extend(new_point);
    }

    *nums.iter().max().expect("Must have maximum")
}

fn print_nums_matrix(nums: &Vec<i32>, width: u32, height: u32) {
    for i in 0..height {
        for j in 0..width {
            let c = nums[translate_2d_to_1d_idx(i, j, width) as usize];
            if c == -1 {
                print!(".");
            } else {
                print!("{}", c);
            }
        }
        println!();
    }
}

fn print_chars_matrix(chars: &Vec<char>, width: u32, height: u32) {
    for i in 0..height {
        for j in 0..width {
            let c = chars[translate_2d_to_1d_idx(i, j, width) as usize];
            print!("{}", c);
        }
        println!();
    }
}

fn is_valid_to_count(chars: &mut Vec<char>, nums: &Vec<i32>, width: u32, _height: u32, x: u32, y: u32) -> bool {
    let mut count = 0;
    for j in 0..y {
        let idx = translate_2d_to_1d_idx(x, j, width) as usize;
        if nums[idx] >= 0 && ['|', 'J', 'L'].contains(&chars[idx]) {
            count += 1;
        }
    }
    if count % 2 == 1 {
        chars[translate_2d_to_1d_idx(x, y, width) as usize] = 'I';
        true
    } else {
        false
    }
}

fn main() {
    let inp = get_input("day10_1_2.inp");
    let height = inp.lines().count() as u32;
    let width = inp.lines().nth(0).unwrap().len() as u32;
    let mut chars = inp.lines().map(|x| x.chars().collect::<Vec<char>>()).flatten().collect::<Vec<char>>();

    let mut nums: Vec<i32> = vec![-1; (width * height) as usize];


    find_ways(&mut chars, &mut nums, width, height);
    // print_nums_matrix(&nums, width, height);
    // print_chars_matrix(&chars, width, height);

    let count = nums.iter().enumerate()
        .filter(|(_, &n)| n < 0)
        .map(|(i, _)| translate_1d_to_2d_idx(i as u32, width))
        .filter(|(x, y)| is_valid_to_count(&mut chars, &nums, width, height, *x, *y))
        .count();

    // print_chars_matrix(&chars, width, height);
    println!("{}", count);
}