use std::fs;
use std::path::{Path};


fn get_input(p: &str) -> String {
    let file_path = Path::new(".").join("inputs").join(p);
    let contents = fs::read_to_string(file_path)
        .expect("Should have been able to read the file");
    contents
}

fn cal_diff_array(nums: Vec<i64>) -> Vec<i64> {
    let mut result: Vec<i64> = vec![];

    for i in 1..nums.len() {
        result.push(nums[i] - nums[i - 1]);
    }

    result
}

fn is_valid_array(nums: &Vec<i64>) -> bool {
    nums.iter().all(|x| *x == 0)
}

fn main() {
    let inp = get_input("day9_1_2.inp");
    let lines: Vec<String> = inp.lines().map(|x| x.to_string()).collect();

    // println!("{:?}", lines);
    let mut sum: i64 = 0;

    for line in lines {
        let mut nums: Vec<i64> = line.split(" ").map(|x| x.parse().expect("Should be convert to i64")).collect();
        let mut last_nums: Vec<i64> = vec![];
        last_nums.push(*(nums.last().expect("Could not be empty")));

        while !is_valid_array(&nums) {
            nums = cal_diff_array(nums);
            last_nums.push(*(nums.last().expect("Could not be empty")));
        }

        let s: i64 = last_nums.iter().sum();
        sum += s;
    }

    println!("{}", sum);
}