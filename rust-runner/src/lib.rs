pub trait Output: ToString {}

macro_rules! allow_output_types {
    ($($t:ty),*) => {
        $(impl Output for $t {})*
    };
}

allow_output_types!(
    u8, u16, u32, u64, u128, usize, // Unsigned integers
    i8, i16, i32, i64, i128, isize, // Signed integers
    f32, f64, // Floats
    String, &str, // Strings
    char, bool
);

pub fn check_result(output: impl Output, expected: &str, part: u8) {
    if output.to_string().trim() != expected.trim() {
        panic!("Output does not match expected for part {}", part);
    }
}
