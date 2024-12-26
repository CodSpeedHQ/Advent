use codspeed_criterion_compat::{criterion_group, criterion_main, Criterion};
use rust_runner::{check_result, Output};
use std::hint::black_box;

paste::paste! {
    #[cfg(not(day_25))]
    use solution::[<day env!("DAY_NUMBER")>]::{part2};
}

#[cfg(not(day_25))]
fn bench_part2(c: &mut Criterion) {
    let mut g = c.benchmark_group(concat!("day", env!("DAY_NUMBER")));
    let input = include_str!("./input.txt");
    #[inline(never)]
    fn routine(input: &str) -> impl Output + '_ {
        part2(black_box(input))
    }
    g.bench_with_input("part2", input, |b, i| b.iter(|| routine(i)));
    let output = routine(input);
    let expected = include_str!("./output-2.txt");
    check_result(output, expected, 2);
}

#[cfg(day_25)]
fn bench_part2(c: &mut Criterion) {
    let mut g = c.benchmark_group(concat!("day", env!("DAY_NUMBER")));
    g.bench_function("part2", |b| b.iter(|| {}));
}


criterion_group!(benches, bench_part2);
criterion_main!(benches);
