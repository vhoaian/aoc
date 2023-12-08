use std::fs;
use std::path::{Path};

fn main() {
    let file_path = Path::new(".").join("inputs").join("day9_1_1.inp");
    println!("In file {:?}", fs::canonicalize(&file_path));

    let contents = fs::read_to_string(file_path)
        .expect("Should have been able to read the file");

    println!("With text:\n{contents}");
}