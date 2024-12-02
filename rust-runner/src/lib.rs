pub fn check_result(output: impl ToString, expected: &str, part: u8) {
    if output.to_string().trim() != expected.trim() {
        panic!("Output does not match expected for part {}", part);
    }
}
