/// This file is used to test that the solution compiles and actually contains day<day_number> part1 and part2 functions
use rust_runner::check_result;

paste::paste! {
    #[cfg(not(day_25))]
    use solution::[<day env!("DAY_NUMBER")>]::{part1, part2};

    #[cfg(day_25)]
    use solution::[<day env!("DAY_NUMBER")>]::part1;
}

#[test]
fn test_build_part_1() {
    let input = "PLACEHOLDER";
    let output = part1(input);
    let expected = "PLACEHOLDER";
    check_result(output, expected, 1);
}

#[cfg(not(day_25))]
#[test]
fn test_build_part_2() {
    let input = "PLACEHOLDER";
    let output = part2(input);
    let expected = "PLACEHOLDER";
    check_result(output, expected, 2);
}
